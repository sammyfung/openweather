from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^airquality/hourly/$', views.hourly_data),
    url(r'^airqualitystation/$', views.station_data),
    url(r'^regional/$', views.regional_weather_data),
]
