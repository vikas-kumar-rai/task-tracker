from django.contrib import admin
from .models import Task, UpdateType, TaskTracker

admin.site.register(Task)
admin.site.register(UpdateType)
admin.site.register(TaskTracker)