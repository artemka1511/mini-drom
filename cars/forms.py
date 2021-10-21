from django.forms import ModelForm
from django import forms
from .models import Car, Images, Model


class CarAddForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['car_user']


class CarImageAddForm(ModelForm):
    image = forms.ImageField(label='Фото', widget=forms.FileInput(attrs={'multiple': 'multiple'}))

    class Meta:
        model = Images
        fields = ('image', )
