from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import Client


class UserAddForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserAddFieldForm(ModelForm):
    class Meta:
        model = Client
        fields = ('phone', )




