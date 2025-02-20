from django.db import models

# Create your models here.
class CityModel(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name
    

class WeatherModel(models.Model):
    date = models.CharField(max_length=50,)
    city = models.CharField(max_length=50)
    temp = models.FloatField()
    desc = models.CharField(max_length=100)
    sun_rise = models.CharField(max_length=50,default='No Data')
    sun_set = models.CharField(max_length=50,default='No Data')