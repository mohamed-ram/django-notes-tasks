from django.contrib import admin

from .forms import TaskForm
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
    list_display = ['title', 'timestamp', 'priority']

    def get_queryset(self, request):
        return Task.objects.all()
        
        
admin.site.register(Task, TaskAdmin)
