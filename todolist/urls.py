from django.urls import path
from todolist.views import show_todolist, login_user, logout_user, register_user, create_task, update_task, delete_task, show_json, add_task

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("create-task/", create_task, name="create_task"),
    path("update/<id>/", update_task, name="update"),
    path("delete/<id>/", delete_task, name="delete"),
    path("json/", show_json, name="show_json"),
    path("add/", add_task, name="add_task"),
]
