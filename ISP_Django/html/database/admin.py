# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from database.models import *


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = ['name', 'date', 'start_time', 'end_time', 'event_type', 'extra_info', 'completed']
    # add filtering by date
    list_filter = ('date',)
    # add search field 
    search_fields = ['name', 'date', 'start_time', 'end_time', 'event_type', 'extra_info', 'completed']

admin.site.register(Event, EventAdmin)