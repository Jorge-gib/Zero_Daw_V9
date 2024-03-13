import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from Registro.models import Orden_reciclaje
from Registro.models import Reserva_orden
from Registro.models import UserModelo
from django.contrib.auth.mixins import LoginRequiredMixin

def geolocalizacion(request, id_orden):
    orden_reciclaje = Orden_reciclaje.objects.filter(id_orden=id_orden).first()

    if orden_reciclaje is None:
        return render(request, 'Api/error_api.html')

    latitud = orden_reciclaje.latitud_posicion_recolector
    longitud = orden_reciclaje.longitud_posicion_recolector

    mapOptions = {
        "center": {"lat": latitud, "lng": longitud},
        "fullscreenControl": True,
        "mapTypeControl": False,
        "streetViewControl": False,
        "zoom": 12,
        "zoomControl": True,
        "maxZoom": 20,
        "mapId": ""
        }

    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitud},{longitud}&key=AIzaSyAeYeyldDKCcpeYVppGwYKzizbDf_HVnSo')

    if response.status_code == 200:
        data = response.json()
        return render(request, 'Api/geolocalizacion.html', {'data': data, 'mapOptions': mapOptions})
    else:
        data = response.json()
        return render(request, 'Api/error_api.html', {'data': data})
    
    
class OrdenListGeolocalizar(LoginRequiredMixin, ListView):
    model = Orden_reciclaje
    template_name = 'Api/orden_geolocalizar.html'
    login_url = '/login/'  # Define la URL de inicio de sesión si el usuario no está autenticado

    def get_queryset(self):
        # Obtén el id del usuario de los parámetros de la URL
        id_user = self.kwargs.get('id_user')
        # Filtra las órdenes por el id_user_id proporcionado
        queryset = Orden_reciclaje.objects.filter(id_user_id=id_user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega las órdenes filtradas al contexto con el nombre 'ordenes'
        context['ordenes'] = self.get_queryset()
        return context
##########################################################################################

def geolocalizacion_ciudadano_orden_normal(request, id_orden):
    orden_reciclaje = Orden_reciclaje.objects.filter(id_orden=id_orden).first()

    if orden_reciclaje is None:
        return render(request, 'Api/error_api.html')

    latitud = orden_reciclaje.latitud_posicion_ciudadano
    longitud = orden_reciclaje.longitud_posicion_ciudadano

    mapOptions = {
        "center": {"lat": latitud, "lng": longitud},
        "fullscreenControl": True,
        "mapTypeControl": False,
        "streetViewControl": False,
        "zoom": 12,
        "zoomControl": True,
        "maxZoom": 20,
        "mapId": ""
        }

    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitud},{longitud}&key=AIzaSyAeYeyldDKCcpeYVppGwYKzizbDf_HVnSo')

    if response.status_code == 200:
        data = response.json()
        return render(request, 'Api/geolocalizacion_3.html', {'data': data, 'mapOptions': mapOptions})
    else:
        data = response.json()
        return render(request, 'Api/error_api.html', {'data': data})
    
############################################################
def geolocalizacion_recolector(request, id_orden):
    orden_reciclaje = Reserva_orden.objects.filter(id_orden=id_orden).first()

    if orden_reciclaje is None:
        return render(request, 'Api/error_api.html')

    latitud = orden_reciclaje.latitud_posicion_recolector
    longitud = orden_reciclaje.longitud_posicion_recolector

    mapOptions = {
        "center": {"lat": latitud, "lng": longitud},
        "fullscreenControl": True,
        "mapTypeControl": False,
        "streetViewControl": False,
        "zoom": 12,
        "zoomControl": True,
        "maxZoom": 20,
        "mapId": ""
        }

    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitud},{longitud}&key=AIzaSyAeYeyldDKCcpeYVppGwYKzizbDf_HVnSo')

    if response.status_code == 200:
        data = response.json()
        return render(request, 'Api/geolocalizacion_4.html', {'data': data, 'mapOptions': mapOptions})
    else:
        data = response.json()
        return render(request, 'Api/error_api.html', {'data': data})
    
    

######################################################################


class ReservaListGeolocalizar_recolector(LoginRequiredMixin, ListView):
    model = Reserva_orden
    template_name = 'Api/orden_geolocalizar_reserva_recolector.html'
    login_url = '/login/'  # Define la URL de inicio de sesión si el usuario no está autenticado

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        return redirect('geolocalizacion_reserva_recolector', id_orden=orden_id)

    def get_queryset(self):
        # Obtiene el ID del usuario actual
        id_user = self.request.user.id
        # Filtra las órdenes por el ID del usuario actual
        queryset = Reserva_orden.objects.filter(id_user_id=id_user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega las órdenes filtradas al contexto con el nombre 'ordenes'
        context['ordenes'] = self.get_queryset()
        return context



    
#####################################################################################
def geolocalizacion_ciudadano(request, id_orden):
    orden_reciclaje = Reserva_orden.objects.filter(id_orden=id_orden).first()

    if orden_reciclaje is None:
        return render(request, 'Api/error_api.html')

    latitud = orden_reciclaje.latitud_posicion_ciudadano
    longitud = orden_reciclaje.longitud_posicion_ciudadano

    mapOptions = {
        "center": {"lat": latitud, "lng": longitud},
        "fullscreenControl": True,
        "mapTypeControl": False,
        "streetViewControl": False,
        "zoom": 12,
        "zoomControl": True,
        "maxZoom": 20,
        "mapId": ""
        }

    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitud},{longitud}&key=AIzaSyAeYeyldDKCcpeYVppGwYKzizbDf_HVnSo')

    if response.status_code == 200:
        data = response.json()
        return render(request, 'Api/geolocalizacion_2.html', {'data': data, 'mapOptions': mapOptions})
    else:
        data = response.json()
        return render(request, 'Api/error_api.html', {'data': data})
    
    

######################################################################################

class OrdenListGeolocalizar_para_ubicar_ciudadano(ListView):
    model = Orden_reciclaje
    template_name = 'Api/orden_geolocalizar_ciudadano.html'

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        return redirect('geolocalizacion_ciudadano_orden', id_orden=orden_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = Orden_reciclaje.objects.all()
        return context
    
######################################################################################

class ReservaListGeolocalizar(ListView):
    model = Reserva_orden
    template_name = 'Api/reserva_geolocalizar.html'

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        return redirect('geolocalizacion_reserva_ciudadano', id_orden=orden_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = Reserva_orden.objects.all()
        return context