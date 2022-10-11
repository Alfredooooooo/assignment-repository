### Perbedaan antara asynchronous programming dengan synchronous programming

Asynchronous programming merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O) protocol. Ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya secara old style / cara lama yaitu dengan eksekusi baris program satu persatu secara hirarki. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau dapat kita sebut secara independen.
<br>
Synchronous programming memiliki pendekatan yang lebih old style. Task akan dieksekusi satu persatu sesuai dengan urutan dan prioritas task. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing task harus menunggu task lain selesai untuk diproses terlebih dahulu.

### Paradigma Event-Driven Programming

Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya.
<br>
Contoh dari penerapan penerapan paradigma ini adalah saat kita menekan tombol 'Add Task' pada modal add task. Disini karena tombol 'Add Task' memilki tipe submit, maka tombol tersebut akan memberikan event submit, jadi untuk melakukan handle untuk hal tersebut, kita lakukan $(elemenSubmit).on('submit', function () {}). Ini bermaksud untuk menjabarkan hal-hal yang perlu dilakukan saat terjadi event submit pada elemen yang memilki class atau id elemenSubmit.
<br>
Hal-hal yang perlu dilakukan ini pada tugas ini adalah memberikan sinyal ke url /todolist/add/ sehingga urls.py akan menangkapnya dan menjalankan fungsi add_task pada views.py untuk melakukan penyimpanan Task baru ke data base sehingga bisa ditampilkan pada browser secara asynchronus. Selain itu dengan JsonResponse pada views.py, kita juga bisa melakukan passing data dan memakai data tersebut sebagai parameter dari success method pada ajax.

### Asynchronous programming pada AJAX.

1. Browser akan memanggil AJAX javascript untuk mengaktifkan XMLHttpRequest dan mengirimkan HTTP Request ke server.
2. XMLHttpRequest dibuat untuk proses pertukaran data di server secara asinkron.
3. Server menerima, memproses, dan mengirimkan data kembali ke browser.
4. Browser menerima data tersebut dan langsung ditampilkan di halaman website, tanpa perlu reload atau membuat halaman baru.

### Cara Implementasi

1. Membuat routing-routing yang dibutuhkan pada urls.py

```shell
    path("update/<id>/", update_task, name="update"),
    path("delete/<id>/", delete_task, name="delete"),
    path("json/", show_json, name="show_json"),
    path("add/", add_task, name="add_task"),
```

2. Buat fungsi pada views.py untuk menghandle request yang datang pada url tersebut

```shell
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
        return JsonResponse({"data": list(task)}, safe=False)
```

3. Buat sebuah folder js di static dan tambahkan suatu file bernama todolist.js dan tulis script berikut ini

```shell
    const setTask = (data, pk) => {
        let d = new Date(data.fields.date.substring(0,10));
        const date = d.toDateString() + ", " + data.fields.date.substring(11, 19)
        if (data.fields.is_finished) {
            $('#appendFinishTrue').append(`
            <div class="card shadow bg-body rounded"">
                <div class="card-header bg-success bg-opacity-10">
                    ${date}
                </div>
                <div class="card-body">
                    <h5 class="card-title">${data.fields.title}</h5>
                    <p class="card-text">${data.fields.description}</p>
                    <a href="/todolist/update/${pk}/" class="btn btn-outline-warning">Unmark As Finished</a>
                    <a class="btn btn-outline-danger mx-1 my-1" id="delete" onclick="deleteTask(${pk})">Delete</a>
                </div>
            </div>
            `)
        } else {
            $('#appendFinishFalse').append(`
            <div class="card shadow bg-body rounded" id="${pk}">
                <div class="card-header bg-success bg-opacity-10">
                    ${date}
                </div>
                <div class="card-body">
                    <h5 class="card-title">${data.fields.title}</h5>
                    <p class="card-text">${data.fields.description}</p>
                    <a href="/todolist/update/${pk}/" class="btn btn-outline-success">Unmark As Finished</a>
                    <a class="btn btn-outline-danger mx-1 my-1" id="delete" onclick="deleteTask(${pk})">Delete</a>
                </div>
            </div>
            `)
        }
    }

    $('#formAddTask').on('submit', (e) => {
        console.log("masuk")
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/todolist/add/",
            data: {
                "title": $('#title').val(),
                "description": $('#description').val(),
            },
            success: (data) => {
                console.log(data)
                // setTask(data, data.fields.id);
                $("#appendInfo").html("");
                $("#appendTask").html("");
                // for(let i = 0; i< data.length; i++) {
                //     setTask(data[i], data[i].pk)
                // }
                getTask()
                $('#exampleModal').modal('hide');
            },
            error: (e) => {
                alert(e);
            }
        })
    })

    const getTask = () => {
        let jumlahData = 0;
        $.ajax({
            url: '/todolist/json/',
            method: 'GET',
            success: (data) => {
                jumlahData = data.length;
                functionGetTask(jumlahData, data);
            }
        })
    }

    const functionGetTask = (jumlahData, data) => {
        if (jumlahData <= 0) {
            $('#appendInfo').append(
                `<div class="container shadow p-3 mb-5 bg-body rounded">
                    <div class="h6">Sepertinya anda belum pernah membuat Task sebelumnya!</div>
                    <p>Belum membuat Task? Ingin Logout?</p>
                        <a href="{% url 'todolist:add_task' %}" class="btn btn-outline-info" id="addTask" data-bs-toggle="modal" data-bs-target="#exampleModal">Buat Task mu</a>
                        <a href="{% url 'todolist:logout' %}" class="btn btn-outline-danger">Logout</a>
                </div>`
            )
        } else {
            console.log("test")
            console.log(jumlahData);
            console.log(data);
            $('#appendInfo').append(
                `<div class="container shadow p-3 mb-5 bg-body rounded">
                    <div class="h6">Berikut adalah task yang sedang dan pernah kamu lakukan!</div>
                    <p>Ingin menambah Task? Ingin Logout?</p>
                        <a href="{% url 'todolist:add_task' %}" class="btn btn-outline-info" id="addTask" data-bs-toggle="modal" data-bs-target="#exampleModal">Tambah Task Baru</a>
                        <a href="{% url 'todolist:logout' %}" class="btn btn-outline-danger">Logout</a>
                </div>`
            )
        }

        if (jumlahData > 0) {
            $('#appendTask').append(`
            <div class="container shadow p-3 mb-5 bg-body rounded">
                <div class="h5 p-2">Yet To Do</div>
                <div class="d-flex justify-content-center align-content-center flex-wrap" id="appendFinishFalse">
            `
            )
            $('#appendTask').append(`
            <div class="container shadow p-3 mb-5 bg-body rounded">
                <div class="h5 p-2">Finished</div>
                <div class="d-flex justify-content-center align-content-center flex-wrap" id="appendFinishTrue">
            `)

            for (let i = 0; i<data.length; i++) {
                let d = new Date(data[i].fields.date.substring(0,10));
                console.log(d)
                const date = d.toDateString() + ", " + data[i].fields.date.substring(11, 19)
                setTask(data[i], data[i].pk)
            }
        }
    }

    const deleteTask = (pk) => {
        console.log("wtf")
        $.ajax({
            url: `/todolist/delete/${pk}/`,
            type: "DELETE",
            success: (data) => {
                console.log("tes")
                $("#appendInfo").html("");
                $("#appendTask").html("");
                // for(let i = 0; i< data.length; i++) {
                //     setTask(data[i], data[i].pk)
                // }
                getTask()
                console.log("lalo")
            },

        })
    }

    $(document).on("DOMContentLoaded", function() {
        getTask();
    })
```

4. Menghubungkan script js dengan todolist.html dengan collectstatic lalu {% load static %} dan hubungkan script dengan:

```shell
    <script src="{% static 'js/todolist.js' %}"></script>
```
