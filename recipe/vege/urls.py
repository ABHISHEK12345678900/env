from django.urls import path
from .views import receipes, delete_receipe, update_receipe
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', receipes, name='receipes'),
    path('delete/<id>/', delete_receipe, name='delete_receipe'),
    path('update/<id>/', update_receipe, name='update_receipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
    urlpatterns += staticfiles_urlpatterns()