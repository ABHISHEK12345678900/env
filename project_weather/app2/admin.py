from django.contrib import admin
from .models import CityModel, WeatherModel

# Register your models here.
admin.site.register(CityModel)

class WeatherModelAdmin(admin.ModelAdmin):
    list_display= ['date', 'city', 'temp', 'desc', 'sun_rise', 'sun_set']

admin.site.register(WeatherModel, WeatherModelAdmin)
