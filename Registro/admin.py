from django.contrib import admin
from .models import Reserva_orden, UserModelo, Calificacion_recolector_ciudadano, Orden_reciclaje, Calificacion_reciclador, Registro_entrega_material

# Registrar los modelos en el panel de administración de Django

# Registrar el modelo Calificacion_recolector_ciudadano
admin.site.register(Calificacion_recolector_ciudadano)

# Registrar el modelo Orden_reciclaje
admin.site.register(Orden_reciclaje)

# Registrar el modelo Calificacion_reciclador
admin.site.register(Calificacion_reciclador)

# Registrar el modelo Registro_entrega_material
admin.site.register(Registro_entrega_material)

# Registrar el modelo UserModelo
admin.site.register(UserModelo)

# Registrar el modelo Reserva_orden
admin.site.register(Reserva_orden)
