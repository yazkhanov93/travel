from django.contrib import admin
from .models import *


@admin.register(ManagerContact)
class ManagerContactAdmin(admin.ModelAdmin):
    list_display = ["title", "whatsapp"]