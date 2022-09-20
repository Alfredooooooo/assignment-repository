from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.


def render_mywatchlist(request):
    data = MyWatchList.objects.all()
    true = 0
    for i in data:
        if (i.watched == True):
            true += 1

    context = {
        "list_watch_list": data,
        "name": "Alfredo Austin",
        "student_id": "2106705865",
        "true_number": true
    }
    return render(request, "mywatchlist.html", context)


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
