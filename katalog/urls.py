# TODO: Implement Routings Here
from django.urls import path
from katalog.views import render_view

# app_name = "katalog"

urlpatterns = [
    path("", render_view, name="render_view"),
]
