# openweather - Open Weather Data Model for Django Web Framework
# Sammy Fung <sammy@sammy.hk>
from __future__ import unicode_literals

from django.db import models


class TropicalCyclone(models.Model):
    AGENCY_CHOICES = (
        ('CWB', 'Central Weather Bureau'),
        ('HKO', 'Hong Kong Observatory'),
        ('JMA', 'Japan Meteorological Agency'),
        ('JTWC', 'Joint Typhoon Warning Center'),
    )
    POS_TYPE_CHOICES = (
        ('C', 'Current'),
        ('F', 'Forecast'),
    )
    TC_TYPE_CHOICES = (
        ('LPA', 'Low Pressure Area'),
        ('TD', 'Tropical Depression'),
        ('TS', 'Tropical Storm'),
        ('TY', 'Typhoon'),
        ('STY', 'Super Typhoon'),
    )
    WIND_UNIT_CHOICES = (
        ('KMH', 'km/h'),
    )
    position_time = models.DateTimeField(verbose_name='Position Time')
    agency = models.CharField(verbose_name='Agency',max_length=4, choices=AGENCY_CHOICES)
    report_time = models.DateTimeField(verbose_name='Report Time')
    code = models.CharField(verbose_name='Code',max_length=3)
    name = models.CharField(verbose_name='Name',max_length=20)
    position_type = models.CharField(verbose_name='Position Type', max_length=1, choices=POS_TYPE_CHOICES)
    cyclone_type = models.CharField(verbose_name='Cyclone Type', max_length=3, choices=TC_TYPE_CHOICES)
    latitude = models.FloatField(verbose_name='Latitude') # N - positive, S - negative
    longitude = models.FloatField(verbose_name='Longitude') # E - positive, W - positive
    pressure = models.IntegerField(verbose_name='Surface Pressure', blank=True, null=True)
    wind_speed = models.IntegerField(verbose_name='Max Sustained Wind Speed', blank=True, null=True)
    gust_speed = models.IntegerField(verbose_name='Max Gust Speed', blank=True, null=True)
    wind_unit = models.CharField(verbose_name='Wind Unit',max_length=3, blank=True, null=True, choices=WIND_UNIT_CHOICES)


class AirQuality(models.Model):
    reptime = models.DateTimeField()
    stationid = models.IntegerField(db_index=True)
    stationcode = models.CharField(max_length=4)
    stationtype = models.CharField(max_length=32,null=True,blank=True)
    name = models.CharField(max_length=32)
    aqhi = models.IntegerField(null=True,blank=True)
    no2 = models.FloatField(null=True,blank=True)
    o3 = models.FloatField(null=True,blank=True)
    so2 = models.FloatField(null=True,blank=True)
    co = models.FloatField(null=True,blank=True)
    pm10 = models.FloatField(null=True,blank=True)
    pm25 = models.FloatField(null=True,blank=True)


class WeatherData(models.Model):
    scraptime = models.DateTimeField()
    reptime = models.DateTimeField()
    station = models.CharField(max_length=3)
    ename = models.CharField(max_length=64)
    cname = models.CharField(max_length=16)
    temperture = models.FloatField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    temperturemax = models.FloatField(null=True, blank=True)
    temperturemin = models.FloatField(null=True, blank=True)
    winddirection = models.CharField(max_length=16,null=True, blank=True)
    windspeed = models.IntegerField(null=True, blank=True)
    maxgust = models.IntegerField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)


class RainfallData(models.Model):
    scraptime = models.DateTimeField()
    reptime = models.DateTimeField()
    ename = models.CharField(max_length=64)
    cname = models.CharField(max_length=16, null=True, blank=True)
    rainfall = models.IntegerField(null=True, blank=True)


class ReportData(models.Model):
    reptime = models.DateTimeField()
    agency = models.CharField(max_length=8)
    reptype = models.CharField(max_length=16)
    lang = models.CharField(max_length=5)
    report = models.TextField()

