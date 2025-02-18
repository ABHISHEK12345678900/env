from django.contrib import admin
from .models import *

# Register your models here.
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ['receipe_name', 'receipe_desc']

admin.site.register(Receipe, ReceipeAdmin)
