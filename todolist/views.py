from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from todolist.models import Task
from todolist.forms import RegisterUserForm, TaskUserForm
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def login_user(request):
    # Mencari method POST pada form method
    if request.method == "POST":
        # Get the username and password from name attribute in input tag
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, "Username atau Password salah!")
    return render(request, "authentication/login.html", {})


def logout_user(request):
    # Melakukan logout
    logout(request)
    response = HttpResponseRedirect(reverse("todolist:login"))
    return response


def register_user(request):
    # Memanggil RegisterUserForm yang merupakan anak dari UserCreationForm
    form = RegisterUserForm()
    if (request.method == "POST"):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request, f"User dengan nama {username} berhasil dibuat")
            # Memindahkan url user ke login agar dapat login
            return redirect("todolist:login")
        else:
            messages.info(
                request, "Ada yang salah dalam proses Registrasi. Silahkan coba lagi!")
    return render(request, "authentication/register.html", {
        "form": form,
    })


@login_required(login_url="/todolist/login/")
def show_todolist(request):
    # Melakukan filter sesuai user pada objek-objek Task
    # data = Task.objects.filter(user=request.user)
    # # Menghitung jumlah data
    # jumlahData = 0
    # for d in data:
    #     jumlahData += 1

    # context = {
    #     "task": data,
    #     "jumlahData": jumlahData,
    # }
    return render(request, "todolist.html", {})


@login_required(login_url="/todolist/login/")
def create_task(request):
    # Memanggil TaskUserForm pada forms.py
    form = TaskUserForm()
    if (request.method == "POST"):
        # Memberikan TaskUserForm informasi-informasi yang diberikan pada user setelah user mengisi form
        form = TaskUserForm(request.POST)
        if (form.is_valid()):
            taskPost = form.save(commit=False)
            form.instance.user = request.user
            taskPost.save()
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
    return render(request, "create_task.html", {"form": form})


def update_task(request, id):
    # Melakukan filter berdasarkan id kepada objek-objek pada model Task
    taskToBeUpdated = Task.objects.filter(pk=id)
    if (taskToBeUpdated[0].is_finished == False):
        # Melakukan update kepada nilai ini langsung ke database agar menghindari static state
        taskToBeUpdated.update(is_finished=True)
    else:
        taskToBeUpdated.update(is_finished=False)

    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url="/todolist/login/")
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def add_task(request):
    if (request.method == "POST"):
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(user=user, title=title, description=description)
        task.save()
        return JsonResponse({"fields": {
            "id": task.id,
            "title": title,
            "description": description,
            "date": task.date,
            "is_finished": task.is_finished,
        }})

@csrf_exempt
def delete_task(request, id):
    print("test")
    taskToBeDeleted = Task.objects.filter(pk=id)
    taskToBeDeleted.delete()
    task = Task.objects.filter(user=request.user).values()
    # listTask = []
    # for t in task:
    #     print(t)
    #     data = {"fields": {
    #         "id": t.get("id"),
    #         "title": t.get("title"),
    #         "description": t.get("description"),
    #         "date": t.get("date"),
    #         "is_finished": t.get("is_finished"),
    #     }}
    #     listTask.append(data)
    return JsonResponse({"data": list(task)}, safe=False)
