from django.contrib import admin

from .models import Task

# Register your models here.
@admin.register(Task)
class Task(admin.ModelAdmin):
    pass