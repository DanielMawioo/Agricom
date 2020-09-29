from django.shortcuts import render
from .models import WorldBorder,Incidence
from django.core.serializers import serialize

# Create your views here.
def index(request):
    return render(request, 'mysite/index.html', {})


def country_datasets(request):
    countries = serialize('geojson', WorldBorder.objects.all())
    return render(request, countries,content_type='json')


def point_datasets(request):
    points = serialize('geojson', Incidence.objects.all())
    return render(request, points,content_type='json',)

