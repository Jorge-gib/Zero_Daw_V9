from django.urls import path, include
from .forms import OrdenUpdateForm, PassUpdateForm, Reserva_ordenForm, RegistroForm, Calificacion_recolector_ciudadanoForm, Orden_reciclajeForm, Calificacion_recicladorForm, Registro_entrega_materialForm
from . import views
from .views import confirmar_comentario, confirmacion4, agregar_calificacion_recolector_ciudadano, ActualizarOrden, MostrarOrdenesParaEliminarView, confirmacion_posicion_recolector, MostrarOrdenesView, TomarOrdenView,somos, validacion_pass, enviar_correo_pass, mensaje, confirmacion3, UserDelete, UserUpdate, confirmacion, Orden_Reserva_List, Autenticar_us, RegistroUsuario, UserList, OrdenList, agregar_orden_reciclaje, registro, agregar_orden_reserva


urlpatterns = [
    
    path('mostrar_ordenes/', MostrarOrdenesView.as_view(), name='mostrar_ordenes'),
    
    path('confirmar_comentario', views.confirmar_comentario, name='confirmar_comentario'),
    
   path('agregar_calificacion_recolector_ciudadano/<int:id_orden>/', views.agregar_calificacion_recolector_ciudadano, name='agregar_calificacion_recolector_ciudadano'),
    
    path('mostrar_ordenes_eliminar/', MostrarOrdenesParaEliminarView.as_view(), name='mostrar_ordenes_eliminar'),
    
    path('tomar_orden/<int:pk>/', TomarOrdenView.as_view(), name='tomar_orden'),
    
    path('confirmacion_posicion_recolector', views.confirmacion_posicion_recolector, name='confirmacion_posicion_recolector'),
     # localhost:8000/registrar
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    
    path('validacion_pass/', views.validacion_pass, name='validacion_pass'),

    path('somos', views.somos, name='somos'),

    # localhost:8000/listar
    path('listar', UserList.as_view(), name="list_user"),
    
     path('enviar_c', views.enviar_correo_pass, name="enviar_c"),
    
    # agregar una carrera    
    path('orden_reciclaje', views.agregar_orden_reciclaje, name="orden_reciclaje"),
    
    path('orden_reserva', views.agregar_orden_reserva, name="orden_reserva"),
    
    path('autenticar_us', Autenticar_us.as_view(), name="autenticar_us"),
    # listar las carreras de la bd
    path('primarykey', views.key, name="primarykey"),
    path('mensaje_pass', views.mensaje, name="mensaje_pass"),
    path('error_validacion', views.error_validacion, name='error_validacion'),
    path('confirmacion3', views.confirmacion3, name="confirmacion3"),
      path('confirmacion4', views.confirmacion4, name="confirmacion4"),
    
    
   
    ##path('registro/', views.registro, name='registro'),

    
   path('verOrdenReciclaje', OrdenList.as_view(), name="verOrdenReciclaje"),
   
   path('confirmacion2', views.confirmacion, name="confirmacion2"),
    
    path('reserva_list', Orden_Reserva_List.as_view(), name="reserva_list"),
    
    
    path('verCalificacionRecolectorCiudadano', views.verCalificacionRecolectorCiudadano, name="verCalificacionRecolectorCiudadano"),
    
    path('verCalificacionReciclador', views.verCalificacionReciclador, name="verCalificacionReciclador"),
    
    path('verRegistroEntregaMaterial', views.verRegistroEntregaMaterial, name="verRegistroEntregaMaterial"),
    

    

    
    # agregar una carrera    
   
     
    # agregar una carrera    
    path('agregar_calificacion_reciclador', views.agregar_calificacion_reciclador, name="agregar_calificacion_reciclador"),
    
    
    # agregar una carrera    
    path('agregar_registro_entrega_material', views.agregar_registro_entrega_material, name="agregar_registro_entrega_material"),
    
    # agregar una carrera    
    path('orden_reciclaje', views.agregar_orden_reciclaje, name="orden_reciclaje"),
    
    # editar una carrera
    path('editar_user/<int:pk>/', views.UserUpdate.as_view(), name='editar_user'),
    
    
     
    
   
    
    
    
    
    # editar una carrera
    path('editar_calificacion_recolector_ciudadano/<int:calificacion_recolector_ciudadano_id>', views.editar_calificacion_recolector_ciudadano, name="editar_calificacion_recolector_ciudadano"),
    
    
     # editar una carrera
    path('editar_calificacion_reciclador/<int:calificacion_reciclador_id>', views.editar_calificacion_reciclador, name="editar_calificacion_reciclador"),
    
    
    # editar una carrera
    path('editar_registro_entrega_matrial/<int:registro_entrega_matrial_id>', views.editar_registro_entrega_matrial, name="editar_registro_entrega_matrial"),
    
    
     # editar una carrera
   
    
    ########################################################################################################################################################
    
    
    # editar una carrera
    path('borrar_user/<int:pk>', UserDelete.as_view(), name="borrar_user"),
    
    
    path('actualizar_orden/<int:pk>', ActualizarOrden.as_view(), name="actualizar_orden"),
    
    
   
    
    # editar una carrera
    path('borrar_calificacion_recolector_ciudadano/<int:calificacion_recolector_ciudadano_id>', views.borrar_calificacion_recolector_ciudadano, name="borrar_calificacion_recolector_ciudadano"),
    
    
     # editar una carrera
    path('borrar_calificacion_reciclador/<int:calificacion_reciclador_id>', views.borrar_calificacion_reciclador, name="borrar_calificacion_reciclador"),
    
    
    # editar una carrera
    path('borrar_registro_entrega_material/<int:registro_entrega_material_id>', views.borrar_registro_entrega_material, name="borrar_registro_entrega_material"),
    
    
     # editar una carrera
    
    
    #########################################################################################################

  




]
