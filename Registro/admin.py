from django.contrib import admin
from .models import Reserva_orden, UserModelo, Calificacion_recolector_ciudadano, Orden_reciclaje, Calificacion_reciclador, Registro_entrega_material

# Register your models here.
admin.site.register(Calificacion_recolector_ciudadano)
admin.site.register(Orden_reciclaje)
admin.site.register(Calificacion_reciclador)
admin.site.register(Registro_entrega_material)
admin.site.register(UserModelo)

admin.site.register(Reserva_orden)