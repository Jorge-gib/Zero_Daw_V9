from django.urls import path
from . import views

urlpatterns = [
     path('geolocalizacion/<int:id_orden>/', views.geolocalizacion, name='geolocalizacion'),
    # Resto de tus URLs
    path('OrdenListGeolocalizar', views.OrdenListGeolocalizar.as_view(), name='OrdenListGeolocalizar')
]