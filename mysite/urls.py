from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('country_datasets/', views.country_datasets, name='country'),
    path('incidence_data/', views.point_datasets, name='incidences'),
]