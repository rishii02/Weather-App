import datetime
import requests
from django.shortcuts import render

def index(request):
    api_key="105c2e7c1c57b10dadc71daa372da439"
    current_w_url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    #forecast_url="api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current, minutely, hourly, alerts&appid={}"

    if request.method == "POST":
        city1= request.POST.get('city1')
        city2= request.POST.get('city2',None)

        w_data= w_and_f(city1, api_key, current_w_url)
        if city2:
            w_data2= w_and_f(city2, api_key, current_w_url)
        else:
            w_data2=None

        return render(request, "weather_app/index.html",context={
            "w_data":w_data,
            "w_data2":w_data2
        })
    else:
        return render(request, "weather_app/index.html")
    

def w_and_f(city, api_key, current_w_url):
    response = requests.get(current_w_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']
    #forecast_response=requests.get(forecast_url.format(lat,lon, api_key)).json()

    data={
        "city":city,
        "temperature": round(response['main']['temp'] - 273.15 ,2),
        "des": response['weather'][0]['description'],
        "icon": response['weather'][0]['icon']
    }

    return data
# Create your views here.
