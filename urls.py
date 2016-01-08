from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^airquality/hourly/$', views.hourly_data),
    url(r'^airqualitystation/$', views.station_data),
)
