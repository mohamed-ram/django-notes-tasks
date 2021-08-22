from django import forms

from .models import Task
from categories.models import Category
from utils.current_request import request


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user', 'slug']
    
    def __init__(self, *args, **kwargs):
        req = request()
        super(TaskForm, self).__init__(*args, **kwargs)
        if req:
            self.fields['category'].queryset = Category.objects.filter(user=req.user)
