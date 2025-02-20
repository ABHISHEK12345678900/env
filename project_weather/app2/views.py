from django.shortcuts import render
import requests
from .models import CityModel

# Create your views here.
def index(request):
    page = 'Add_and_check_City_stats'
    appid = 'c551cdbebc5f82e27cea98c4a2012026'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    
    if request.method == 'POST':
        city = request.POST.get('city')
        params = {'q': city, 'appid': appid, 'units': 'metric'}
        r = requests.get(url=URL, params=params)
        resp = r.json()

        if not CityModel.objects.filter(city_name=city).exists():
            CityModel.objects.create(city_name=city)
            message = 'city added to DB'
        else:
            message = city + ' already present in DB'

        description = resp['weather'][0]['description']
        icon = resp['weather'][0]['icon']
        temp = resp['main']['temp']

        context = {
            'page': page,
            'city': city,
            'message': message,
            'desc': description,
            'icon': icon,
            'temp': temp
        }

        return render(request, 'app2/city.html', context)
    
    else :

        return render(request, 'app2/city.html')