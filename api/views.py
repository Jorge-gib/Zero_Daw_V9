from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from Registro.models import Orden_reciclaje
import requests

def geolocalizacion(request):
    if request.method == 'GET':
        user_id = request.user.id  # Obtener el ID del usuario autenticado
        
        # Obtener la instancia del modelo Orden_reciclaje_recolector asociada al usuario
        orden_reciclaje = Orden_reciclaje.objects.filter(id_user=user_id).first()

        if orden_reciclaje is None:
            return render(request, 'Api/error_api.html')
        
        latitud = float(orden_reciclaje.latitud_posicion_recolector)
        longitud = float(orden_reciclaje.longitud_posicion_recolector)
        
        # Modificar las coordenadas en mapOptions
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
        
        # Llamar a la API de geolocalización con las coordenadas proporcionadas
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitud},{longitud}&key=AIzaSyAeYeyldDKCcpeYVppGwYKzizbDf_HVnSo')

        if response.status_code == 200:
            data = response.json()

            # Procesar los datos de respuesta según tus necesidades
            # Por ejemplo, puedes extraer la dirección u otros detalles de interés

            return render(request, 'Api/geolocalizacion.html', {'data': data, 'mapOptions': mapOptions})
        else:
            data = response.json()
            return render(request, 'Api/error_api.html', {'data': data})
        
    else:
        data = response.json()
        return render(request, 'Api/error_api.html', {'data': data})