from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post_todo/', post_todo, name= 'post_todo'),
    path('get_todo/', get_todo, name= 'get_todo')
]