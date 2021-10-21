from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(verbose_name='Номер телефона')

