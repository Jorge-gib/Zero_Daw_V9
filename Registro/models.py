from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserModelo(AbstractUser):
    TIPO_USUARIO = (
        ('Recolector', 'Recolector'),
        ('Reciclador', 'Reciclador'),
        ('Ciudadano', 'Ciudadano'),
        ('Operario municipalidad', 'Operario municipalidad'),
    )

    rut = models.CharField(max_length=10, null=True, blank=True)
    dv = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)  
    direccion = models.CharField(max_length=50, null=True, blank=True)
    comuna = models.CharField(max_length=80, null=True, blank=True)
    codigo_postal = models.IntegerField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    validacion_recolector = models.BooleanField(default=False)  # Campo booleano con valor predeterminado False

    licencia_automotriz = models.ImageField(upload_to='licencias/', blank=True, null=True)
    segundo_nombre_madre = models.CharField(max_length=100,null=True,blank=True)
    tipo_usuario = models.CharField(max_length=200, blank=False, null=True, choices=TIPO_USUARIO)
    new_password1 = models.CharField(max_length=50, null=True)
    new_password2 = models.CharField(max_length=50, null=True)
    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')
    validacion_recolector = models.BooleanField(default=False)

    def __str__(self):
        return self.rut if self.rut else self.username

class Orden_reciclaje(models.Model):
    id_user = models.ForeignKey(UserModelo, on_delete=models.CASCADE)
    id_orden = models.AutoField(primary_key=True)
    fecha_orden = models.DateField()
    rut_recolector = models.CharField(max_length=10, null=True)
    cantidad_plastico = models.IntegerField(default=0)
    cantidad_vidrio = models.IntegerField(default=0)
    cantidad_carton = models.IntegerField(default=0)
    cantidad_aluminio = models.IntegerField(default=0)
    cantidad_metal = models.IntegerField(default=0)
    cantidad_electrodomesticos = models.IntegerField(default=0)
    latitud_posicion_ciudadano = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud_posicion_ciudadano = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitud_posicion_recolector = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud_posicion_recolector = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    estado = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id_orden)

    def get_rut_recolector(self):
        return self.rut_recolector if self.rut_recolector else ''
class Reserva_orden(models.Model):
    id_user = models.ForeignKey(UserModelo, on_delete=models.CASCADE)
    id_orden = models.AutoField(primary_key=True)
    fecha_orden = models.DateField()
    rut_recolector = models.CharField(max_length=10, null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cantidad_plastico = models.IntegerField(default=0)
    cantidad_vidrio = models.IntegerField(default=0)
    cantidad_carton = models.IntegerField(default=0)
    cantidad_aluminio = models.IntegerField(default=0)
    cantidad_metal = models.IntegerField(default=0)
    cantidad_electrodomesticos = models.IntegerField(default=0)
    latitud_posicion_ciudadano = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud_posicion_ciudadano = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitud_posicion_recolector = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud_posicion_recolector = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    estado = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id_orden)
    def get_rut_recolector(self):
        return self.rut_recolector if self.rut_recolector else ''
    

class Recepcion_desechos(models.Model):
    id_orden = models.ForeignKey(Orden_reciclaje, on_delete=models.CASCADE)
    id_registro = models.AutoField(primary_key=True)
    fecha_registro = models.DateField()
    cantidad_plastico = models.IntegerField(default=0)
    cantidad_vidrio = models.IntegerField(default=0)
    cantidad_carton = models.IntegerField(default=0)
    cantidad_aluminio = models.IntegerField(default=0)
    cantidad_metal = models.IntegerField(default=0)
    cantidad_electrodomesticos = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_registro)

class Recepcion_desechos_reserva(models.Model):
    id_orden = models.ForeignKey(Reserva_orden, on_delete=models.CASCADE)
    id_registro = models.AutoField(primary_key=True)
    fecha_registro = models.DateField()
    cantidad_plastico = models.IntegerField(default=0)
    cantidad_vidrio = models.IntegerField(default=0)
    cantidad_carton = models.IntegerField(default=0)
    cantidad_aluminio = models.IntegerField(default=0)
    cantidad_metal = models.IntegerField(default=0)
    cantidad_electrodomesticos = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_registro)

class Calificacion_recolector_ciudadano(models.Model):
    id_orden = models.ForeignKey(Orden_reciclaje, on_delete=models.CASCADE)
    id_calificacion = models.AutoField(primary_key=True)
    calificacion_estrellas_ciudadano = models.FloatField(null=True)
    calificacion_estrellas_recolector = models.FloatField(null=True)
    opinion_servicio_ciudadano = models.CharField(max_length=400, null=True)
    opinion_servicio_recolector = models.CharField(max_length=400, null=True)

    def __str__(self):
        return str(self.id_calificacion)

class Calificacion_recolector_ciudadano_reserva(models.Model):
    id_orden = models.ForeignKey(Reserva_orden, on_delete=models.CASCADE)
    id_calificacion = models.AutoField(primary_key=True)
    calificacion_estrellas_ciudadano = models.FloatField(null=True)
    calificacion_estrellas_recolector = models.FloatField(null=True)
    opinion_servicio_ciudadano = models.CharField(max_length=400, null=True)
    opinion_servicio_recolector = models.CharField(max_length=400, null=True)

    def __str__(self):
        return str(self.id_calificacion)

class Registro_pago(models.Model):
    
    id_registro = models.ForeignKey(Recepcion_desechos, on_delete=models.CASCADE)
    id_pago = models.AutoField(primary_key=True)
    fecha_pago = models.DateField()
    telefono_reciclador = models.IntegerField(default=0)
    total_material_reciclado = models.IntegerField(default=0)
    monto_pago = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_pago)

class Registro_pago_reserva(models.Model):
    id_registro = models.ForeignKey(Recepcion_desechos_reserva, on_delete=models.CASCADE)
    id_pago = models.AutoField(primary_key=True)
    fecha_pago = models.DateField()
    telefono_reciclador = models.IntegerField(default=0)
    total_material_reciclado = models.IntegerField(default=0)
    monto_pago = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_pago)



    
    