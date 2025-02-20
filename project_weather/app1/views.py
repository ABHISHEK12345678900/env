from django.shortcuts import render
import os
import requests
import datetime

# Create your views here.
def index(request):
    API_KEY = open('C:/Users/abhis/OneDrive/Desktop/env/project_weather/API_KEY.txt', 'r').read()
    current_weather_url = 'http://openweathermap.org/data/2.5/weather?name={}&appid={}'
    print(current_weather_url)
    forecast_url = 'http://openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'

    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data, daily_forecast = fetch_weather_and_forecast(city, API_KEY, current_weather_url, forecast_url)
        context = {
            'weather_data': weather_data,
            'daily_forecast': daily_forecast
        }

        return render(request, 'app1/index.html', context)
    
    else:
        return render(request, 'app1/index.html')
    


def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    print(response)
    lat, lon = response['coord']['lat'], response['coord']['lon']
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'desc': response['weather']['description'],
        'icon': response['weather'][0]['icon']
    }

    daily_forecast = []

    for daily_data in forecast_response['daily'][:5]:
        daily_forecast.append({
            'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
            'min_temp': round(daily_data['temp']['min'] -273.15, 2),
            'max_temp': round(daily_data['temp']['max'] -273.15, 2),
            'desc': daily_data['weather'][0]['description'],
            'icon': daily_data['weather'][0]['icon']
        })

    return weather_data, daily_forecast