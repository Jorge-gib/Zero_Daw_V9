# admin.py
from django.contrib import admin
from .models import Reserva_orden, UserModelo, Registro_pago_reserva, Registro_pago, Calificacion_recolector_ciudadano_reserva, Calificacion_recolector_ciudadano, Orden_reciclaje, Recepcion_desechos, Recepcion_desechos_reserva

admin.site.register(Calificacion_recolector_ciudadano)
admin.site.register(Calificacion_recolector_ciudadano_reserva)
admin.site.register(Orden_reciclaje)
admin.site.register(Recepcion_desechos)
admin.site.register(Recepcion_desechos_reserva)
admin.site.register(UserModelo)
admin.site.register(Reserva_orden)
admin.site.register(Registro_pago_reserva)
admin.site.register(Registro_pago)
