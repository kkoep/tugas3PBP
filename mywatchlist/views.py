from django.shortcuts import render
from mywatchlist.models import Watchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_watchlist = Watchlist.objects.all()
    context = {
    'item_watchlist': data_watchlist,
    'nama': 'Yosua'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = Watchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Watchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Watchlist.objects.filter(pk=id)
    # Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Watchlist.objects.filter(pk=id)
    # Jika XML
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")