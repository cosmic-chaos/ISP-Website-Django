# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_type = models.CharField(max_length=30)
    extra_info = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    assigned = models.ManyToManyField(User)
   # users_request = models.ManyToManyField(User)
   # users_accept = models.ManyToManyField(User)

