## Heroku App Link

[Todolist Heroku](https://pbpassignment.herokuapp.com/todolist/)
<br>
[Create Task Heroku](https://pbpassignment.herokuapp.com/todolist/create-task/)
<br>
[Login Heroku](https://pbpassignment.herokuapp.com/todolist/login/)
<br>
[Register Heroku](https://pbpassignment.herokuapp.com/todolist/register/)
<br>
username: pbpdummy1, pbpdummy2
<br>
password: pbptugaslab

# Tugas 4

## Jawaban Pertanyaan

#### Apa kegunaan {% csrf_token %} pada elemen <form>?

Cross-Site Request Forgery (CSRF) merupakan serangan yang pada umumnya dilakukan penyerang yang memaksa pengguna untuk melakukan tindakan yang tidak diinginkan pada aplikasi web yang telah diakses pengguna tersebut (telah login/autentikasi). Maka Django mengimplementasi csrf_token guna untuk menghindari CSRF attack yang mungkin akan digunakan oleh penyerang. Tag csrf_token akan generate token pada server sesaat kita melakukan rendering pada halaman/browser, serta melakukan filter request yang masuk pada browser (jika request tersebut tidak mempunyai token, maka request tersebut tidak akan dieksekusi).

#### Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Django tetap akan mendisplay form tersebut, namun sekalinya kita melakukan submit form, maka akan ada HTTP Request 403 Forbidden karena verifikasi CSRF gagal dan request diabaikan. Alasan terjadinya 403 Forbidden ini adalah CSRF Token yang tidak dapat ditemukan

#### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?

Bisa, jadi kita bisa membuat elemen form secara manual (tentu saja dengan {% csrf_token %}) dan menyimpan data-data form tersebut melalui method save.

#### Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Misalkan kita diberikan sebuah class Model anggap saja Person serta melakukan migrasi skema model ini ke database.
Kita bisa melakukannya dengan:<br>

1. Membuat form terlebih dahulu pada direktori template dan anggap nama filenya adalah "dummy.html"
2. Membuat url yang menghubungi template tersebut dengan suatu fungsi bernama someFunction
3. Mendesain fungsi someFunction agar dapat memproses form tersebut
   <br>
   Contoh dummy.html:

```shell
    ...
    <form action="" method="POST">
        {% csrf_token %}
        <input type="text" placeholder="Siapa namamu?" name="nama">
        <input type="text" placeholder="Apa hobimu?" name="hobi">
        <input type="text" placeholder="Kamu tinggal dimana?" name="domisili">
        <input type="submit" class="btn btn-primary" value="Submit"></input>
    </form>
    ...
```

Contoh someFunction:

```shell
    def someFunction(request):
        if request.method == "POST":
            name = request.POST.get("nama")
            hobby = request.POST.get("hobi")
            domisili = request.POST.get("domisili")
            p = Person(name=name, hobby=hobby, domisili=domisili)
            p.save()
            return HttpResponseRedirect("/dummy.html/")
        else:
            return render(request, "dummy.html", {})
```

Dengan ini form telah tersimpan dalam database dan akan terlihat hasilnya apabila dibuat semacam tabel untuk mendisplay data.

#### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1. Membuat suatu Model class bernama SomeModel dengan field-field yang mendefinisikan class tersebut serta isilah
2. Data yang telah diisi akan tersubmit dan dapat diambil oleh fungsi yang mempunyai parameter request dan mempunyai perkondisian seperti request.method == "POST"
3. Lalu setelah masuk ke perkondisian tersebut, terdapat beberapa cara untuk menyimpan data tersebut dalam data base, yaitu:
   <br>
   Cara pertama:

```shell
    from .forms import SomeForm
    from .models import SomeModel
    from django.http import HttpResponseRedirect

    def someFunction(request):
        form = SomeForm()
        if request.method == "POST":
            form = SomeForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(suatuURL)
        return render(request, suatuURL, {"form": form})
```

atau

```shell
    from .forms import SomeForm
    from .models import SomeModel
    from django.http import HttpResponseRedirect

    def SomeFunction(request):
        form = SomeForm()
        if request.method == "POST":
            form = SomeForm(request.POST)
            if form.is_valid():
                field1 = form.cleaned_data["field1"]
                field2 = form.cleaned_data["field2"]
                ...
                mdl = SomeModel(field1=field1, field2=field2, ...)
                mdl.save()
                return HttpResponseRedirect(suatuURL)
        return render(request, suatuURL, {"form": form})
```

Cara diatas harus dilakukan dengan cara membuat sebuah Form class bernama SomeForm dan memanggilnya. Dalam class SomeForm tersebut terdapat subclass bernama Meta yang mendefinisikan bagaimana konfigurasi outer class dari subclass tersebut dan inilah visualisasinya:

```shell
    class SomeForm(ModelForm):
        ...
        class Meta:
            model = SomeModel
            ...
        ...
```

Cara kedua:

```shell
    from .models import SomeModel
    from django.http import HttpResponseRedirect

    def someFunction(request):
        if request.method == "POST":
            field1 = request.POST.get("field1")
            field2 = request.POST.get("field2")
            ...
            mdl = SomeModel(field1=field1, field2=field2, ...)
            mdl.save()
            return HttpResponseRedirect(suatuURL)
        return render(request, suatuURL, {})
```

Cara kedua tidak melibatkan pembuatan suatu Form class pada forms.py sehingga hanya melibatkan model dalam penyimpanan datanya.<br><br>

4. Pemunculan data dari database dapat dilakukan dengan cara memanggil sebuah/beberapa model dan memanggil fungsi objects pada model tersebut dan memilih apakah ingin semua data yang ditampilkan atau semacamnya

```shell
    from .models import SomeModel
    def someFunction(request):
        ...
        data = SomeModel.objects.all() # Memanggil semua data
        ...
        context = {
            "data": data,
            ...
        }
        return render(request, suatuURL, context)
```

5. Data telah muncul pada template HTML!

## Sebelum implementasi:

1. Menjalankan perintah berikut untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```

2. Menyelakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

3. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

4. Membuat aplikasi baru dengan menjalankan command berikut:

   ```shell
   django-admin startapp todolist
   ```

## Cara mengimpementasi:

1. Menambahkan path mywatchlist di direktori project_django pada file settings.py dan pada file urls.py

```shell
INSTALLED_APPS = [
    ...
    'katalog',
    'mywatchlist',
    'todolist',
]
```

```shell
    urlpatterns = [
        ...
        path('katalog/', include('katalog.urls')),
        path('mywatchlist/', include('mywatchlist.urls')),
        path('todolist/', include('django.contrib.auth.urls')),
        path('todolist/', include('todolist.urls')),
    ]
```

2. Membuat Class Task dengan parameter models.Model pada models.py untuk membuat skema model tabel yang akan dibuat:

```shell
    class Task(models.Model):
        # if user is deleted, delete objects (not class) related to user as well
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateTimeField()
        title = models.CharField(max_length=120)
        description = models.TextField(blank=True, null=True)
        is_finished = models.BooleanField(default=False)
```

3. Buka terminal (cmd) dan jalankan perintah berikut untuk melakukan migrasi skema model ke database Django lokal:

   ```shell
   python manage.py makemigrations
   ```

4. Jalankan perintah berikut untuk menerapkan skema model diatas:

   ```shell
   python manage.py migrate
   ```

5. Setelah itu pertama membuat template navigation bar dalam bentuk HTML yang bernama navbar.html dan memasang semua url yang diperlukan pada directory template:

   ```shell
   <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
       <div class="container-fluid">
           <div>
               <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                   <li class="nav-item">
                       <a class="navbar-brand" href="{% url 'todolist:show_todolist' %}">To do List</a>
                       <a class="navbar-brand" href="{% url 'todolist:create_task' %}">Create Task</a>
                   </li>
               </ul>
           </div>
           <div>
               <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                   <li class="nav-item">
                       {% if user.is_authenticated %}
                           <span class="navbar-brand">Logged in as {{user.username}}</span>
                           <span class="navbar-brand">|</span>
                           <a class="navbar-brand" href="{% url 'todolist:logout' %}">Logout</a>
                       {% else %}
                           <a class="navbar-brand" href="{% url 'todolist:login' %}">Login</a>
                           <a class="navbar-brand" href="{% url 'todolist:register' %}">Register</a>
                       {% endif %}
                   </li>
               </ul>
           </div>

       </div>
   </nav>
   ```

6. Selanjutnya membuat template registrasi dalam bentuk HTML yang bernama register.html pada directory baru yaitu authentication dan melakukan include navbar:

```shell
    {% extends 'base.html' %}


    {% block content %}
        {% include 'navbar.html' %}
        <div class="container p-xl-3">
            {% if form.errors %}
                <div class="alert alert-warning alert-dismissible fade show" role="alert">
                    Ada yang salah dalam proses Registrasi. Silahkan coba lagi!
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            {% endif %}
        </div>
        <div class="container shadow p-3 mb-5 bg-body rounded">
            <div class="h1 mb-3">Register Page</div>
            <form action="{% url 'todolist:register' %}" method="POST">
                {% csrf_token %}

                {{form.as_p}}

                <input type="submit" name="submit" value="Daftar" class="btn btn-primary"/>
            </form>
        </div>
    {% endblock content %}
```

7. Membuat template login dalam bentuk HTML yang bernama login.html pada direktori baru yaitu authentication dan melakukan include navbar:

```shell
    {% extends 'base.html' %}

    {% block content %}
        {% include 'navbar.html' %}
        <div class="container p-xl-3">
            {% if messages %}
                {% for message in messages %}
                    {% if message %}
                        <div class="alert alert-info alert-dismissible fade show" role="alert">
                            {{message}}
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                    {% endif %}
                {% endfor %}
            {% endif %}
        </div>
        <div class="container shadow p-3 mb-5 bg-body rounded">
            <div class="h1 mb-3">Login Page</div>
            <form action="" method="POST">
                {% csrf_token %}
                <div class="mb-4">
                    <input type="text" class="form-control" name="username" placeholder="Username">
                </div>
                <div class="mb-3">
                    <input type="password" class="form-control" placeholder="Password" name="password">
                </div>
                <button type="submit" class="btn btn-primary" value="login">Login</button>
            </form>
        </div>
    {% endblock content %}
```

8. Membuat template task to do dalam bentuk HTML yang bernama todolist.html dan melakukan include navbar:

```shell
    {% extends 'base.html' %}

    {% block content %}
        {% include 'navbar.html' %}
        <div class="m-3"></div>
        {% if jumlahData == 0 %}
            <div class="container shadow p-3 mb-5 bg-body rounded">
                <p>Sepertinya anda belum pernah membuat Task sebelumnya!</p>
                Belum membuat Task? <a href="{% url 'todolist:create_task' %}">Buat Task mu</a>
            </div>

        {% else %}
            <div class="container shadow p-3 mb-5 bg-body rounded">
                <div class="h5 p-2">Yet To Do</div>
                    {% for data in task %}
                        {% if data.is_finished == False %}
                            <div class="card shadow bg-body rounded">
                                    <div class="card-header">
                                        {{data.date}}
                                    </div>
                                    <div class="card-body">
                                        <h5 class="card-title">{{data.title}}</h5>
                                        <p class="card-text">{{data.description}}</p>
                                        <a href="{% url 'todolist:update' data.id %}" class="btn btn-outline-success">Mark As Finished</a>
                                        <a href="{% url 'todolist:delete' data.id %}" class="btn btn-outline-danger">Delete</a>
                                    </div>
                            </div>
                        {% endif %}
                    {% endfor %}
            </div>

            <div class="container shadow p-3 mb-5 bg-body rounded">
                <div class="h5 p-2">Finished</div>
                    {% for data in task %}
                        {% if data.is_finished %}
                            <div class="card">
                                    <div class="card-header">
                                        {{data.date}}
                                    </div>
                                    <div class="card-body">
                                        <h5 class="card-title">{{data.title}}</h5>
                                        <p class="card-text">{{data.description}}</p>
                                        <a href="{% url 'todolist:update' data.id %}" class="btn btn-outline-warning">Unmark As Finished</a>
                                        <a href="{% url 'todolist:delete' data.id %}" class="btn btn-outline-danger">Delete</a>
                                    </div>
                            </div>
                        {% endif %}
                    {% endfor %}
            </div>

        {% endif %}
    {% endblock content %}
```

9. Serta membuat template create task to do dalam bentuk HTML yang bernama create_task.html dan melakukan include navbar:

```shell
    {% extends 'base.html' %}

    {% block content %}
        {% include 'navbar.html' %}

        <div class="container shadow p-3 mb-5 mt-4 bg-body rounded">
            <div class="h1 mb-3">Create Your To Do List</div>
            <form action="" method="POST">
                {% csrf_token %}

                {{form.as_p}}

                <input type="submit" name="submit" value="Daftar" class="btn btn-primary"/>
            </form>
        </div>
    {% endblock content %}
```

10. Setelah membuat template, lakukan routing url pada urls.py (membuat urls.py terlebih dahulu) kepada template-template tersebut dan membuat pseudo function yang nantinya akan diimplementasikan pada views.py:

```shell
    from django.urls import path
    from todolist.views import show_todolist, login_user, logout_user, register_user, create_task, update_task, delete_task

    app_name = "todolist"

    urlpatterns = [
        path("", show_todolist, name="show_todolist"),
        path("login/", login_user, name="login"),
        path("logout/", logout_user, name="logout"),
        path("register/", register_user, name="register"),
        path("create-task/", create_task, name="create_task"),
        path("update/<id>", update_task, name="update"),
        path("delete/<id>", delete_task, name="delete"),
    ]
```

11. Setelah itu masuk pada views.py dan buatlah fungsi fungsi yang telah ditulis pada urls.py agar saat client merequest pada browser untuk membuka url, url tersebut dapat berfungsi dengan baik:

```shell
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    from django.contrib.auth.decorators import login_required
    from django.contrib.auth import authenticate, login
    from django.contrib.auth import logout
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    from django.shortcuts import render
    from todolist.models import Task
    from todolist.forms import RegisterUserForm, TaskUserForm

    # Create your views here.


    def login_user(request):
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
        logout(request)
        response = HttpResponseRedirect(reverse("todolist:login"))
        return response


    def register_user(request):
        form = RegisterUserForm()
        if (request.method == "POST"):
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                messages.success(
                    request, f"User dengan nama {username} berhasil dibuat")
                return redirect("todolist:login")
            else:
                messages.info(
                    request, "Ada yang salah dalam proses Registrasi. Silahkan coba lagi!")
        return render(request, "authentication/register.html", {
            "form": form,
        })


    @login_required(login_url="/todolist/login/")
    def show_todolist(request):
        data = Task.objects.filter(user=request.user)
        jumlahData = 0
        for d in data:
            jumlahData += 1

        context = {
            "task": data,
            "jumlahData": jumlahData,
        }
        return render(request, "todolist.html", context)


    @login_required(login_url="/todolist/login/")
    def create_task(request):
        form = TaskUserForm()
        if (request.method == "POST"):
            form = TaskUserForm(request.POST)
            if (form.is_valid()):
                taskPost = form.save(commit=False)
                form.instance.user = request.user
                taskPost.save()
                response = HttpResponseRedirect(reverse("todolist:show_todolist"))
                return response
        return render(request, "create_task.html", {"form": form})


    def update_task(request, id):
        print(id)
        taskToBeUpdated = Task.objects.filter(pk=id)
        if (taskToBeUpdated[0].is_finished == False):
            taskToBeUpdated.update(is_finished=True)
        else:
            taskToBeUpdated.update(is_finished=False)

        return HttpResponseRedirect(reverse("todolist:show_todolist"))


    def delete_task(request, id):
        taskToBeDeleted = Task.objects.filter(pk=id)
        taskToBeDeleted.delete()
        return redirect(reverse("todolist:show_todolist"))
```

12. Membuat file bernama forms.py dan mengisi form-form yang diinginkan dan yang ingin dimodifikasi:

```shell
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User
    from django import forms
    from django.forms import ModelForm
    from todolist.models import Task


    class RegisterUserForm(UserCreationForm):
        class Meta:
            model = User
            fields = ("username", "password1", "password2")

        def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)

            self.fields["username"].widget.attrs["class"] = "form-control"
            self.fields["password1"].widget.attrs["class"] = "form-control"
            self.fields["password2"].widget.attrs["class"] = "form-control"
            self.fields["username"].widget.attrs["placeholder"] = "Username"
            self.fields["password1"].widget.attrs["placeholder"] = "Password"
            self.fields["password2"].widget.attrs["placeholder"] = "Retype Password"


    class TaskUserForm(ModelForm):
        class Meta:
            model = Task
            fields = ("title", "description")

            labels = {
                "title": "",
                "description": "",
            }

            widgets = {
                "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Task Title"}),
                "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Task Description"}),
            }
```

13. Terakhir mengakses admin dengan membuatnya terlebih dahulu pada cmd dengan nama admin dan password 123

```shell
python manage.py createsuperuser
```

14. Lalu masuk pada admin.py lalu tambahkan model Class pada database yang dapat diamati

```shell
    from django.contrib import admin
    from todolist.models import Task
    # Register your models here.

    admin.site.register(Task)
```

# Tugas 5

## Jawaban Pertanyaan

### Perbedaan dari Inline, Internal, dan External CSS

##### Inline CSS

- Inline diaplikasikan ke single tag dari dokumen HTML
- Inline style declaration juga diletakkan di dalam tag tersebut

##### Advantage Inline CSS

- CSS mudah untuk diinsert ke HTML page, sehingga metode ini cocok untuk dipakai jika kita ingin melakukan testing, melihat perubahan, atau bahkan melakukan debugging pada website kita
- Kita tidak perlu membuat file terpisah untuk CSS

#### Disadvantage Inline CSS

- Menambahkan CSS ke setiap tag pada HTML memerlukan waktu yang banyak dan membuat struktur HTML kita tidak bersih
- Melakukan styling elemen dapat merubah ukuran page kita dan waktu download

##### Internal CSS

- Internal CSS diaplikasikan ke seluruh HTML file tersebut (satu HTML saja) tapi tidak diaplikasikan ke file HTML lainnya
- Biasanya internal CSS diletakkan dan diurung di dalam <head></head> tag dan dipanggil dengan <style></style>

#### Advantage Internal CSS

- Kita dapat menggunakan ID dan class selector pada file ktia
- Kita tidak perlu membuat file terpisah untuk CSS
- Struktur akan lebih rapih dibanding inline CSS
- Tidak memerlukan waktu yang banyak ketimbang menggunakan inline CSS

#### Disadvantage Internal CSS

- Menambahkan CSS pada HTML document secara langsung akan menambah ukuran page (byte) dan mempengaruhi kecepatan download

#### External CSS

- External CSS diaplikasikan ke seluruh HTML file tersebut dan bisa diaplikasikan juga ke file HTML lainnya
- External CSS ditulis dalam file berbeda dengan extension css dan dipanggil dengan <link rel="stylesheet" href="URLnya">
- External CSS memudahkan kita untuk memberikan tampilan yang konsisten pada keseluruhan HTML file yang kita punya

#### Advantage External CSS

- Ukuran HTML (dalam byte) akan lebih kecil dibandingkan menggunakan kedua cara diatas
- Kita bisa menggunakan file CSS yang sama untuk berbagai HTML file
- Struktur akan lebih rapih dibanding inline dan internal CSS
- Tidak memerlukan waktu yang banyak ketimbang menggunakan inline dan internal CSS

#### Disadvantage External CSS

- Page yang dirender mungkin saja akan lebih lama sampai external CSS berhasil di load
- Linking ke berbagai CSS file bisa saja meningkatkan waktu download yang diperlukan

### HTML Tag yang saya ketahui

- <html>: Tag pembuka untuk membuat dokumen HTML
- <head>: Informasi meta tentang dokumen
- <title>: Membuat judul halaman yang nantinya akan ditampilkan di browser
- <body>: Tempat dibuatnya semua konten website menggunakan HTML
- <h1> s/d <h6>:  Membuat judul atau heading
- <hr>: Memisahkan konten (biasanya ditampilkan garis pembatas)
- <p>:  Membuat paragraf
- <br>: Membuat garis baru
- <style>: Atribut untuk elemen styling pada HTML
- <b>: Membuat teks tebal
- <strong>: Membuat teks penting
- <i>: Membuat teks miring
- <img>: Elemen untuk mendefinisikan gambar
- <form>: Membuat formulir untuk mengumpulkan input pengguna
- <input>: Membuat tipe inputan pada form yang akan dibuat
- <textarea>: Elemen untuk mendefinisikan field input
- <label>: Memberikan label pada elemen input
- <button>: Membuat Button
- <table>: Membuat tabel pada web
- <div>: container

### Tipe-tipe CSS selector yang saya ketahui

- .namaClass: Memilih semua elemen dengan nama class="namaClass"
- .namaClass1.namaClass2: Memilih semua elemen dengan nama nameClass1 dan nameClass2 pada class attribute
- .namaClass1 .namaClass2: Memilih class bernama namaClass2 yang merupakan anak dari namaClass1
- #id: Memilih id dengan nama id pada atribut id pada tag html
- :active : Memilih link yang aktif
- :checked : Melihat apakah checkbutton sudah tercheck
- :hover : Saat mouse di hover pada suatu element, akan dilakukan sesuatu

### Cara mengimplementasi checkpoint diatas

Saya menambahkan class center yang berisi:

```shell
    .center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    }
```

Serta melakukan import font pada body

```shell
    @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;400;700&display=swap");

    body {
    font-family: "Poppins", sans-serif;
    font-weight: 300;
    font-size: 15px;
    line-height: 1.7;
    color: #444;
    overflow-x: hidden;
    }
```

Saya juga menggunakan method hover yaitu:

```shell
    a {
    cursor: pointer;
    transition: all 200ms linear;
    }
    a:hover {
    text-decoration: none;
    }
    .link {
    color: #102770;
    text-decoration: none;
    }
    .link:hover {
    color: #ffeba7;
    }

    .btn-hover {
    transition: all 200ms linear;
    -webkit-transition: all 200ms linear;
    padding: 0.4rem 2.5rem;
    background-color: #444;
    color: #eee;
    box-shadow: 0 8px 24px 0 rgba(255, 235, 167, 0.2);
    outline: none;
    }
    .btn-hover:active,
    .btn-hover:focus {
    background-color: #102770;
    color: #44a1;
    box-shadow: 0 8px 24px 0 rgba(16, 39, 112, 0.2);
    outline: none;
    }
    .btn-hover:hover {
    background-color: #102770;
    color: #44a1;
    box-shadow: 0 8px 24px 0 rgba(16, 39, 112, 0.2);
    }
```

Saya menambahkan background color pada date dan menambahkan opacity tertentu. Selain itu saya juga menggunakan bootstrap untuk mendesain card tersebut beserta flex. Saya juga melakukan pekerjaan bonus yaitu saat mouse dihover saya akan scaling card menjadi 1.2x nya.
