from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_desc = models.TextField()
    receipe_image = models.ImageField(default='No Image')