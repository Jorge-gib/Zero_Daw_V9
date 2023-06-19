from django.urls import path
from . import views

urlpatterns = [
    path('geolocalizacion/', views.geolocalizacion, name='geolocalizacion'),
    # Resto de tus URLs
]