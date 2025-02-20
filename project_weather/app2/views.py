from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, timedelta
import requests
from .models import CityModel, WeatherModel
from astral import LocationInfo 
from astral.sun import sun
from geopy.geocoders import Nominatim
import folium


# Create your views here.
def index(request):
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    page = 'Add_and_check_City_stats'
    appid = 'c551cdbebc5f82e27cea98c4a2012026'
    URL1 = 'https://api.openweathermap.org/data/2.5/weather'
    
    
    if request.method == 'POST':
        city = request.POST.get('city')

        sunrise, sunset , latitude, longitude= get_sun_times(city)

        params = {'q': city, 'appid': appid, 'units': 'metric'}
        r = requests.get(url=URL1, params=params)
        resp = r.json()

        if not CityModel.objects.filter(city_name=city).exists():
            CityModel.objects.create(city_name=city)
            message = 'city added to DB'
        else:
            message = city + ' already present in DB'

        description = resp['weather'][0]['description']
        icon = resp['weather'][0]['icon']
        temp = resp['main']['temp']

        m = folium.Map(location=[latitude, longitude], zoom_start=12)
        # Add a marker (pointer) for the city
        folium.Marker(
            [latitude, longitude],
            popup=f"{city}",
            tooltip="Click for more info"
        ).add_to(m)
        map_html = m._repr_html_()

        context = {
            'date': dt,
            'page': page,
            'city': city,
            'message': message,
            'desc': description,
            'icon': icon,
            'temp': temp,
            'sunrise': sunrise,
            'sunset': sunset,
            'latitude': latitude,
            'longitude': longitude,
            'map': map_html,
        }

        WeatherModel.objects.create(date= dt, city= city, temp= temp, desc= description, sun_rise= sunrise.strftime('%Y-%m-%d %H:%M'), sun_set= sunset.strftime('%Y-%m-%d %H:%M'))

        return render(request, 'app2/city.html', context)
    
    else :

        return render(request, 'app2/city.html')
    
def load_city_map(request):
    pass


def get_location_details(city_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(city_name)
    if not location:
        raise ValueError("City not found")
    # For simplicity, assume region and timezone are known or can be set
    region = "India"  # or determine dynamically
    timezone = "Asia/Kolkata"  # you could use other libraries to determine timezone
    return location.latitude, location.longitude, region, timezone

def get_sun_times(city_name):
    latitude, longitude, region, timezone = get_location_details(city_name)
    location = LocationInfo(city_name, region, timezone, latitude, longitude)
    today = date.today()
    sun_info = sun(location.observer, date=today)
    # Add 5 hours to the sunrise and sunset times
    sunrise = sun_info['sunrise'] + timedelta(hours=5, minutes=30)
    sunset = sun_info['sunset'] + timedelta(hours=5, minutes=30)
    
    return sunrise, sunset, latitude, longitude