from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import WorldBorder,Incidence


# Create your views here.
def index(request):
    return render(request, 'mysite/index.html', {})


def country_datasets(request):
    countries = serialize('geojson', WorldBorder.objects.all())
    return HttpResponse(countries,content_type='json')


def point_datasets(request):
    points = serialize('geojson', Incidence.objects.all())
    return HttpResponse(points,content_type='json',)

