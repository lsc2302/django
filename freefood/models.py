from django.db import models
from django.utils.timezone import now
import datetime


# Create your models here.


class Event(models.Model):
    Etitle = models.CharField(max_length=30, default="free food")
    Etype = models.CharField(max_length=20, default="Pizza")
    Estart = models.DateTimeField(default=now)
    Eend = models.DateTimeField(default=now)
    Eopen = models.CharField(max_length=40, default="all")
    Eplace = models.CharField(max_length=40, default="school")
    Edescription = models.CharField(max_length=300, default='no description')
    Ersvps = models.IntegerField(default=0)


class User(models.Model):
    username = models.CharField(max_length=20,default="user")
    password = models.CharField(max_length=20,default="N/A")
    location = models.CharField(max_length=40,default="N/A")
    email = models.CharField(max_length=40,default="N/A")
    tel = models.CharField(max_length=15,default="N/A")
    EventsRegister = models.ManyToManyField('Event')
