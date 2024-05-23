from django import forms
from .models import MyModel


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'email', 'message']
        labels = {
            'name': "Ім'я",
            'email': 'Пошта',
            'message': 'Повідомлення'
        }
