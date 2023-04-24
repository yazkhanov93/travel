from django.contrib import admin
from .models import *


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 0


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ["title","category"]
    inlines = [TourImageInline]


@admin.register(TourCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]