from django.contrib import admin
from .models import *


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ["user", "point"]


@admin.register(PointEarned)
class PointEarnedAdmin(admin.ModelAdmin):
    list_display = ["user", "point", "description", "date"]


@admin.register(PointSpent)
class PointSpentAdmin(admin.ModelAdmin):
    list_display = ["user", "point", "description", "date"]