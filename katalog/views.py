from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.


def render_view(request):
    list_katalog = CatalogItem.objects.all()
    rendered_fields = {
        "list_field": list_katalog,
        "name": "Alfredo Austin",
        "student_id": "2106705865",
    }
    return render(request, "katalog.html", rendered_fields)
