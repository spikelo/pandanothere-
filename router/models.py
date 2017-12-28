from django.db import models
from django.utils.timezone import now
from django.contrib.auth.admin import User


class Router(models.Model):
    date = models.DateField(default=now)
    model = models.CharField(max_length=15)
    SN = models.CharField(max_length=20)
    username = models.ForeignKey('Username', on_delete=models.SET_NULL,null=True)
    manager = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.model


class Username(models.Model):
    login = models.CharField(max_length=15)
    contract = models.CharField(max_length=15)
    def __str__(self):
        return self.login

