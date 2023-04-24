from django.contrib import admin
from .models import *


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 0


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ["title", "star_count", "city"]
    inlines = [HotelImageInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["title"]

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["title"]

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["title"]