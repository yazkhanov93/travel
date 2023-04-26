from django.contrib import admin
from .models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "point"]


@admin.register(TaskDone)
class TaskDoneAdmin(admin.ModelAdmin):
    list_display = ["task", "user", "date", "checked"]