from django.urls import path
from Registro import views
from . import views

# URLs para la geolocalización de órdenes
urlpatterns = [
    # Ruta para la geolocalización de una orden específica
    path('geolocalizacion/<int:id_orden>/', views.geolocalizacion, name='geolocalizacion'),
    
    # Ruta para la geolocalización de una reserva de ciudadano
    path('geolocalizacion_reserva_ciudadano/<int:id_orden>/', views.geolocalizacion_ciudadano, name='geolocalizacion_reserva_ciudadano'),
    
    # Ruta para la geolocalización de una reserva de recolector
    path('geolocalizacion_reserva_recolector/<int:id_orden>/', views.geolocalizacion_recolector, name='geolocalizacion_reserva_recolector'),
    
    # Ruta para la geolocalización de una orden específica para ciudadanos
    path('geolocalizacion_ciudadano_orden/<int:id_orden>/', views.geolocalizacion_ciudadano_orden_normal, name='geolocalizacion_ciudadano_orden'),
]

# URLs para listar y geolocalizar órdenes y reservas
urlpatterns += [
    # Ruta para listar y geolocalizar órdenes vinculando por id de usuario
    path('OrdenListGeolocalizar/<int:id_user>/', views.OrdenListGeolocalizar.as_view(), name='OrdenListGeolocalizar'),
    
    # Ruta para listar y geolocalizar reservas
    path('ReservaListGeolocalizar', views.ReservaListGeolocalizar.as_view(), name='ReservaListGeolocalizar'),
    
    # Ruta para listar y geolocalizar órdenes para ubicar ciudadanos
    path('OrdenListGeolocalizar_para_ubicar_ciudadano', views.OrdenListGeolocalizar_para_ubicar_ciudadano.as_view(), name='OrdenListGeolocalizar_para_ubicar_ciudadano'),
    
    # Ruta para listar y geolocalizar órdenes para ubicar recolectores
    path('OrdenListGeolocalizar_para_ubicar_recolector/<int:id_user>/', views.ReservaListGeolocalizar_recolector.as_view(), name='OrdenListGeolocalizar_para_ubicar_recolector'),
]
