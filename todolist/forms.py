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
