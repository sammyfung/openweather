# openweather - Open Weather Data Model Admin for Django Web Framework
# Sammy Fung <sammy@sammy.hk>
from django.contrib import admin
from openweather.models import TropicalCyclone, AirQuality, WeatherData, RainfallData, ReportData


class TropicalCycloneAdmin(admin.ModelAdmin):
    list_display = ('report_time', 'agency', 'code', 'name', 'position_type', 'position_time', 'latitude', 'longitude',
                    'cyclone_type', 'wind_speed', 'gust_speed', 'wind_unit', 'pressure')
    # list_filter = ('agency', 'position_type', 'cyclone_type', 'code')
    search_fields = ['name', 'agency', 'code', 'cyclone_type', 'position_type']


class AirQualityAdmin(admin.ModelAdmin):
     list_display = ('reptime', 'stationid', 'stationcode', 'stationtype', 'name','aqhi','no2','o3','so2','co','pm10','pm25')
     list_filter = ['stationid', 'stationtype']


class WeatherDataAdmin(admin.ModelAdmin):
    list_display = (
    'scraptime', 'reptime', 'station', 'ename', 'cname', 'temperture', 'humidity', 'temperturemax', 'temperturemin',
    'winddirection', 'windspeed', 'maxgust', 'pressure')
    list_filter = ['station', 'winddirection']


class RainfallDataAdmin(admin.ModelAdmin):
    list_display = ('scraptime', 'reptime', 'ename', 'cname', 'rainfall')
    list_filter = ['ename']


class ReportDataAdmin(admin.ModelAdmin):
    list_display = ('reptime', 'agency', 'reptype', 'lang', 'report')
    list_filter = ['agency', 'reptype', 'lang']


admin.site.register(TropicalCyclone, TropicalCycloneAdmin)
admin.site.register(AirQuality, AirQualityAdmin)
admin.site.register(WeatherData, WeatherDataAdmin)
admin.site.register(RainfallData, RainfallDataAdmin)
admin.site.register(ReportData, ReportDataAdmin)
