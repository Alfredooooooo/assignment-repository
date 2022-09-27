from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# default to 1 day from now


def get_default_my_date():
    return datetime.now()


class Task(models.Model):
    # if user is deleted, delete objects (not class) related to user as well
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # Referencing the function not instantiating the function
    date = models.DateTimeField(default=get_default_my_date)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)
