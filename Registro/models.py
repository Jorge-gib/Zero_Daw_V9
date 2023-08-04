from django.db import models
from datetime import datetime
#from Usuario.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission



class UserModelo(AbstractUser):
    TIPO_USUARIO = (
        ('Recolector', 'Recolector'),
        ('Reciclador', 'Reciclador'),
        ('Ciudadano', 'Ciudadano'),
        ('Operario_municipalidad', 'Operario_municipalidad'),
    )
   
    rut = models.CharField(max_length=10)
    dv = models.IntegerField()
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()  # Cálculo aproximado de la edad en años
    direccion = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()
    telefono = models.IntegerField()
    licencia_automotriz = models.ImageField(
        'Licencia automotriz', upload_to='licencias/', blank=True, null=True)
    segundo_nombre_madre = models.CharField(max_length=100)
    tipo_usuario = models.CharField(
        max_length=200, blank=False, null=True, choices=TIPO_USUARIO)
    new_password1 = models.CharField(max_length=50, null=True)
    new_password2 = models.CharField(max_length=50, null=True)
    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')
    
    
    def __str__(self):
        return self.rut
    
    

class Orden_reciclaje(models.Model):
    id_user = models.ForeignKey(UserModelo, on_delete=models.CASCADE)
    id_orden = models.AutoField(primary_key=True)
    fecha_orden = models.DateField()
    cantidad_plastico = models.IntegerField(default=0)
    cantidad_vidrio = models.IntegerField(default=0)
    cantidad_carton = models.IntegerField(default=0)
    cantidad_aluminio = models.IntegerField(default=0)
    latitud_posicion_ciudadano = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud_posicion_ciudadano = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitud_posicion_recolector = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud_posicion_recolector = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    estado = models.CharField(max_length=200, null=True)
     
    


    def __str__(self):
        return str(self.id_orden)
    
class Reserva_orden(models.Model):
    id_user = models.ForeignKey(UserModelo, on_delete=models.CASCADE)
    id_orden = models.AutoField(primary_key=True)
    fecha_orden = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cantidad_plastico = models.IntegerField(default=0)
    cantidad_vidrio = models.IntegerField(default=0)
    cantidad_carton = models.IntegerField(default=0)
    cantidad_aluminio = models.IntegerField(default=0)
    latitud_posicion_ciudadano = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud_posicion_ciudadano = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitud_posicion_recolector = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud_posicion_recolector = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    estado = models.CharField(max_length=200, null=True)
   
     
    


    def __str__(self):
        return str(self.id_orden)
    

     
    


    
    

    
class Registro_entrega_material(models.Model):
    id_user = models.ForeignKey(UserModelo, on_delete=models.CASCADE)
    id_registro = models.AutoField(primary_key=True)
    fecha_registro = models.DateField()
    cantidad_plastico = models.IntegerField(default=0)
    cantidad_vidrio = models.IntegerField(default=0)
    cantidad_carton = models.IntegerField(default=0)
    cantidad_aluminio = models.IntegerField(default=0)
    def __str__(self):
        return str(self.ID_registro)
    
    
class Calificacion_recolector_ciudadano(models.Model):
    id_orden = models.ForeignKey(Orden_reciclaje, on_delete=models.CASCADE)
    id_calificacion = models.AutoField(primary_key=True)
    calificacion_estrellas_ciudadano = models.FloatField(null=True)
    calificacion_estrellas_recolector = models.FloatField(null=True)
    opinion_servicio_ciudadano = models.CharField(max_length=400, null=True)
    opinion_servicio_recolector = models.CharField(max_length=400, null=True)
    def __str__(self):
        return str(self.id_calificacion)


class Calificacion_reciclador(models.Model):
    id_registro = models.ForeignKey(Registro_entrega_material, on_delete=models.CASCADE)
    id_calificacion = models.AutoField(primary_key=True)
    calificacion_estrellas = models.FloatField()
    opinion_servicio = models.CharField(max_length=400)
    def __str__(self):
        return str(self.id_calificacion)
