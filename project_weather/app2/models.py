from django.db import models

# Create your models here.
class CityModel(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name
