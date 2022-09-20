from django.urls import path
from mywatchlist.views import render_mywatchlist, show_json, show_json_by_id, show_xml, show_xml_by_id

app_name = "mywatchlist"

urlpatterns = [
    path("html/", render_mywatchlist, name="render_mywatchlist"),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]
