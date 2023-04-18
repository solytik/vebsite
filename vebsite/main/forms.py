from . models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'name', 'task', 'text']

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            "text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
        }