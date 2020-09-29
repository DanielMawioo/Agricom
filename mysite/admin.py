from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Incidence, WorldBorder

@admin.register(Incidence)
class ShopAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


@admin.register(WorldBorder)
class WorldBorderAdmin(LeafletGeoAdmin):
    list_display = ('name', 'region')
