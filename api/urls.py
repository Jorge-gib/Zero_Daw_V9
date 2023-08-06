from django.urls import path
from . import views

urlpatterns = [
     path('geolocalizacion/<int:id_orden>/', views.geolocalizacion, name='geolocalizacion'),
     
     path('geolocalizacion_reserva_ciudadano/<int:id_orden>/', views.geolocalizacion_ciudadano, name='geolocalizacion_reserva_ciudadano'),
     
     
     path('geolocalizacion_reserva_recolector/<int:id_orden>/', views.geolocalizacion_recolector, name='geolocalizacion_reserva_recolector'),
     
     
     path('geolocalizacion_ciudadano_orden/<int:id_orden>/', views.geolocalizacion_ciudadano_orden_normal, name='geolocalizacion_ciudadano_orden'),
     
    # Resto de tus URLs
    path('OrdenListGeolocalizar', views.OrdenListGeolocalizar.as_view(), name='OrdenListGeolocalizar'),
    
    path('ReservaListGeolocalizar', views.ReservaListGeolocalizar.as_view(), name='ReservaListGeolocalizar'),
    
    path('OrdenListGeolocalizar_para_ubicar_ciudadano', views.OrdenListGeolocalizar_para_ubicar_ciudadano.as_view(), name='OrdenListGeolocalizar_para_ubicar_ciudadano'),
    
    ################################################################################################################
    
    path('OrdenListGeolocalizar_para_ubicar_recolector', views.ReservaListGeolocalizar_recolector.as_view(), name='OrdenListGeolocalizar_para_ubicar_recolector'),
]