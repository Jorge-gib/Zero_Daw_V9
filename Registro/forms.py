from django import forms
from .models import Reserva_orden, UserModelo, Calificacion_recolector_ciudadano, Orden_reciclaje, Calificacion_reciclador, Registro_entrega_material
from django.contrib.auth import get_user_model
from django.shortcuts import render
import itertools
from itertools import chain
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.db import models
class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = UserModelo
        fields = [
            'first_name',
            'last_name',
            'edad',
            'direccion',
            'codigo_postal',
            'telefono',
            'licencia_automotriz'
            
        ]
        
class PassUpdateForm(forms.ModelForm):
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir nueva contraseña', widget=forms.PasswordInput)

    class Meta:
        model = UserModelo
        fields = [
            'rut',
            'segundo_nombre_madre',
            'new_password1',
            'new_password2',
            
        ]
            
           
            
            
        





class RegistroForm(UserCreationForm):
    rut = forms.CharField(max_length=10)
    dv = forms.IntegerField()
    edad = forms.IntegerField()
    direccion = forms.CharField(max_length=50)
    codigo_postal = forms.IntegerField()
    telefono = forms.IntegerField()
    licencia_automotriz = models.CharField(max_length=200, null=True)
    segundo_nombre_madre = models.CharField(max_length=100)
    tipo_usuario = forms.ChoiceField(choices=UserModelo.TIPO_USUARIO)

    class Meta:
        model = UserModelo
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'rut',
            'dv',
            'edad',
            'direccion',
            'codigo_postal',
            'telefono',
            'licencia_automotriz',
            'segundo_nombre_madre',
            'tipo_usuario',
        ]
        labels = {
            'id': 'ID',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Repita Contraseña',
            'rut': 'Rut',
            'dv': 'DV',
            'edad': 'Edad',
            'direccion': 'Dirección',
            'codigo_postal': 'Código postal',
            'telefono': 'Teléfono',
            'licencia_automotriz': 'Licencia automotriz',
            'segundo_nombre_madre': 'Segundo nombre madre',
            'tipo_usuario': 'Tipo usuario',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'dv': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'licencia_automotriz': forms.FileInput(attrs={'class': 'form-control'}),
            'segundo_nombre_madre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
        }
             
             
             
        





        
class Calificacion_recolector_ciudadanoForm(forms.ModelForm):
    class Meta:
        model = Calificacion_recolector_ciudadano
        fields = ['id_orden', 'id_calificacion', 'calificacion_estrellas_ciudadano', 'calificacion_estrellas_recolector', 'opinion_servicio_ciudadano', 'opinion_servicio_recolector']

        labels = {
            
            'id_orden': 'ID orden',
            'id_calificacion': 'ID calificacion',
            'calificacion_estrellas_ciudadano': 'Calificacion estrellas ciudadano',
            'calificacion_estrellas_recolector': 'Calificacion estrellas recolector',
            'opinion_servicio_ciudadano': 'Opinion servicio ciudadano',
            'opinion_servicio_recolector': 'Opinion servicio recolector',

        }
        widgets = {
           
            'id_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'id_calificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'calificacion_estrellas_ciudadano': forms.TextInput(attrs={'class': 'form-control'}),
            'calificacion_estrellas_recolector': forms.TextInput(attrs={'class': 'form-control'}),
            'opinion_servicio_ciudadano': forms.TextInput(attrs={'class': 'form-control'}),
            'opinion_servicio_recolector': forms.TextInput(attrs={'class': 'form-control'}),
           
           
        }



class Calificacion_recicladorForm(forms.ModelForm):
    class Meta:
        model = Calificacion_reciclador
        fields = ['id_registro', 'id_calificacion', 'calificacion_estrellas', 'opinion_servicio']

        labels = {
            'id_registro': 'ID registro',
            'id_calificacion': 'ID calificacion',
            'calificacion_estrellas': 'Calificacion_estrellas',
            'opinion_servicio': 'Opinion_servicio',

        }
        widgets = {
            'id_registro': forms.TextInput(attrs={'class': 'form-control'}),
            'id_calificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'calificacion_estrellas': forms.TextInput(attrs={'class': 'form-control'}),
            'opinion_servicio': forms.TextInput(attrs={'class': 'form-control'}),
           
           
        }


class Registro_entrega_materialForm(forms.ModelForm):
    class Meta:
        model = Registro_entrega_material
        fields = ['id_user', 'id_registro', 'fecha_registro',
                  'tipo_material', 'cantidad_material']

        labels = {
            'id_user': 'ID_user',
            'id_registro': 'ID_registro',
            'fecha_registro': 'Fecha_registro',
            'tipo_material': 'Tipo_material',
            'cantidad_material': 'Cantidad_material',

        }
        widgets = {
            'id_user': forms.TextInput(attrs={'class': 'form-control'}),
            'id_registro': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_material': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_material': forms.TextInput(attrs={'class': 'form-control'}),
           
           
        }
class Posicion_recolectorForm(forms.ModelForm):
    class Meta:
        Model = Orden_reciclaje
        fields = ['latitud_posicion_recolector',
                  'longitud_posicion_recolector']

        labels = {
           
            'latitud_posicion_recolector': 'Latitud_posicion_recolector',
            'longitud_posicion_recolector': 'Longitud_posicion_recolector',
           

        }
        widgets = {
            
            'latitud_posicion_recolector': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud_posicion_recolector': forms.TextInput(attrs={'class': 'form-control'}),
            
           
           
        }
        
         
        
        
class Orden_reciclajeForm(forms.ModelForm):
    class Meta:
        model = Orden_reciclaje
        fields = ['id_user', 'id_orden',
                  'fecha_orden', 'tipo_material', 'cantidad_material', 'latitud_posicion_ciudadano',
                  'longitud_posicion_ciudadano']

        labels = {
            'id_user': 'ID user',
            'id_orden': 'ID_orden',
            'fecha_orden': 'Fecha_orden',
            'tipo_material': 'Tipo_material',
            'cantidad_material': 'Cantidad_material',
            'latitud_posicion_ciudadano': 'Latitud_posicion_ciudadano',
            'longitud_posicion_ciudadano': 'Longitud_posicion_ciudadano',
           

        }
        widgets = {
            'id_user': forms.TextInput(attrs={'class': 'form-control'}),
            'id_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_material':forms.Select(choices="TIPO_MATERIAL",attrs={'class':'form-control'}),
            'cantidad_material': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud_posicion_ciudadano': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud_posicion_ciudadano': forms.TextInput(attrs={'class': 'form-control'}),
            
           
           
        }
        

class Reserva_ordenForm(forms.ModelForm):
    class Meta:
        model = Reserva_orden
        fields = ['id_user', 'id_orden',
                  'fecha_orden','hora_inicio', 'hora_fin', 'tipo_material', 'cantidad_material', 'latitud_posicion_ciudadano',
                  'longitud_posicion_ciudadano']

        labels = {
            'id_user': 'ID user',
            'id_orden': 'ID_orden',
            'fecha_orden': 'Fecha_orden',
            'hora_inicio': 'Hora de inicio reserva',
            'hora_inicio': 'Hora de termino de reserva', 
            'tipo_material': 'Tipo_material',
            'cantidad_material': 'Cantidad_material',
            'latitud_posicion_ciudadano': 'Latitud_posicion_ciudadano',
            'longitud_posicion_ciudadano': 'Longitud_posicion_ciudadano',
           

        }
        widgets = {
            'id_user': forms.TextInput(attrs={'class': 'form-control'}),
            'id_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_fin': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_material':forms.Select(choices="TIPO_MATERIAL",attrs={'class':'form-control'}),
            'cantidad_material': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud_posicion_ciudadano': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud_posicion_ciudadano': forms.TextInput(attrs={'class': 'form-control'}),
            
           
           
        }





