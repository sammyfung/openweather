from django.http import HttpResponse, Http404
from openweather.models import AirQuality, WeatherData
from datetime import datetime, timedelta
import json, pytz


def hourly_data(request):
    query_time = request.GET.get('time', 0)
    if query_time == 0:
        query_time = AirQuality.objects.order_by('-reptime')[0].reptime.isoformat()
    json_data = []
    for station in AirQuality.objects.values().filter(reptime = query_time):
        hkt = pytz.timezone('Asia/Hong_Kong')
        station['reptime'] = station['reptime'].astimezone(hkt).isoformat()
        json_data = json_data + [ station ]
    if len(json_data) > 0:
        return HttpResponse(json.dumps(json_data), content_type="application/json")
    else:
        return Http404


def station_data(request):
    # 1. All stations in past hour or Individual station in past 24 hours.
    # 2. 24 hours data if start_time is supplied by user.
    request_id = request.GET.get('id',0)
    start_time = request.GET.get('start', 0)
    if start_time != 0:
        oldest_time = datetime.strptime(start_time, "%Y%m%d")
    if request_id != 0:
        if start_time == 0:
            oldest_time = datetime.now() - timedelta(days=1)
        data = AirQuality.objects.values().filter(stationid = request_id, reptime__gte = oldest_time)[0:24]
    else:
        if start_time == 0:
            oldest_time = datetime.now() - timedelta(hours=2)
        data = AirQuality.objects.values().filter(reptime__gte = oldest_time)

    # return in JSON data format or 404 if no data.
    if len(data) == 0:
        raise Http404
    json_data = []
    for hourly in data:
        hkt = pytz.timezone('Asia/Hong_Kong')
        # hourly['reptime'] = hourly['reptime'].astimezone(hkt).__str__()
        hourly['reptime'] = hourly['reptime'].astimezone(hkt).isoformat()
        json_data = json_data + [ hourly ]
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def regional_weather_data(request):
    # 1. Latest measurement at all stations or individual stations in past 24 hours.
    # 2. 24 hour data if start_time is supplied by user.
    station_id = request.GET.get('id', 0)
    start_time = request.GET.get('start', 0)
    if start_time != 0:
        oldest_time = datetime.strptime(start_time, "%Y%m%d")
    if station_id != 0:
        if start_time == 0:
            oldest_time = datetime.now() - timedelta(days=1)
        data = WeatherData.objects.values().filter(station = station_id, reptime__gte = oldest_time)[0:24]
    else:
        if start_time == 0:
            oldest_time = datetime.now() - timedelta(hours=2)
        data = WeatherData.objects.values().filter(reptime__gte = oldest_time)

    # return in JSON data format or 404 if no data.
    if len(data) == 0:
        raise Http404
    json_data = []
    # latest_time = WeatherData.objects.order_by('-reptime')[0].reptime.isoformat()
    # for station in WeatherData.objects.values().filter(reptime = latest_time):
    for station in data:
        hkt = pytz.timezone('Asia/Hong_Kong')
        station['reptime'] = station['reptime'].astimezone(hkt).isoformat()
        station['scraptime'] = station['scraptime'].astimezone(hkt).isoformat()
        json_data = json_data + [ station ]
    return HttpResponse(json.dumps(json_data), content_type="application/json")

