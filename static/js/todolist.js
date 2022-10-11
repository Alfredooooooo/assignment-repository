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
            $('#exampleModal').modal('hide');
            getTask()
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