from django.conf.urls import *
from ISP.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/$', signin, name="signin"),
    url(r'^profile/$', profile, name="profile"),
    url(r'^$', index, name="index"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^ongoing/$', ongoing, name="ongoing"),
    url(r'^past/$', past, name="past"),
    url('^', include('django.contrib.auth.urls')),
]
