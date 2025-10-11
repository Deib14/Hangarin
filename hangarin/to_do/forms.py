from django.forms import ModelForm
from django import forms
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
        }