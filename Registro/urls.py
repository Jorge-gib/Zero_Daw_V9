from django.urls import path
from . import views
from .views import (
    # Importaciones de vistas
    MostrarOrdenesCalificarCiudadanoReservaView,
    MostrarOrdenesCalificarRecolectorReservaView,
    MostrarReservaParaEliminarView,
    ActualizarReserva,
    MostrarReservaView,
    TomarReservaView,
    zero_daw,
    video_reciclaje,
    MostrarOrdenesCalificarRecolectorView,
    agregar_calificacion_recolector_ciudadano2,
    MostrarOrdenesParaEliminarView,
    confirmar_comentario,
    confirmacion4,
    agregar_calificacion_recolector_ciudadano,
    ActualizarOrden,
    MostrarOrdenesView,
    TomarOrdenView,
    somos,
    validacion_pass,
    enviar_correo_pass,
    mensaje,
    confirmacion3,
    UserDelete,
    UserUpdate,
    confirmacion,
    Orden_Reserva_List,
    Autenticar_us,
    RegistroUsuario,
    UserList,
    OrdenList,
    agregar_orden_reciclaje,
    registro,
    agregar_orden_reserva,
)

urlpatterns = [
    # URLS con sus respectivos nombres y vistas asociadas
    
    # Mostrar lista de órdenes
    path('mostrar_ordenes/', MostrarOrdenesView.as_view(), name='mostrar_ordenes'),
    
    # Mostrar lista de reservas
    path('mostrar_reserva/', MostrarReservaView.as_view(), name='mostrar_reserva'),
    
    # Confirmar comentario
    path('confirmar_comentario', views.confirmar_comentario, name='confirmar_comentario'),
    
    # Página Zero DAW
    path('zero_daw', views.zero_daw, name='zero_daw'),
    
    # Agregar calificación para recolector
    path('agregar_calificacion_recolector/<int:id_orden>/', views.agregar_calificacion_recolector_reserva, name='agregar_calificacion_recolector_ciudadano'),
    
    # Agregar calificación para ciudadano en reserva
    path('agregar_calificacion_ciudadano_reserva/<int:id_orden>/', views.agregar_calificacion_ciudadano_reserva, name='agregar_calificacion_ciudadano_reserva'),
    
    # Agregar calificación para recolector y ciudadano
    path('agregar_calificacion_recolector_ciudadano/<int:id_orden>/', views.agregar_calificacion_recolector_ciudadano, name='agregar_calificacion_recolector_ciudadano'),
    
    # Otra ruta para agregar calificación para recolector y ciudadano
    path('agregar_calificacion_recolector_ciudadano2/<int:id_orden>/', views.agregar_calificacion_recolector_ciudadano2, name='agregar_calificacion_recolector_ciudadano2'),
    
    # Mostrar órdenes para eliminar
    path('mostrar_ordenes_eliminar/', MostrarOrdenesParaEliminarView.as_view(), name='mostrar_ordenes_eliminar'),
    
    # Mostrar reservas para eliminar
    path('mostrar_ordenes_eliminar_reserva/', MostrarReservaParaEliminarView.as_view(), name='mostrar_ordenes_eliminar_reserva'),
    
    # Mostrar órdenes para calificar recolector
    path('mostrar_ordenes_calificar_recolector/', MostrarOrdenesCalificarRecolectorView.as_view(), name='mostrar_ordenes_calificar_recolector'),
    
    # Mostrar órdenes para calificar recolector en reserva
    path('mostrar_ordenes_calificar_recolector_reserva/', MostrarOrdenesCalificarRecolectorReservaView.as_view(), name='mostrar_ordenes_calificar_recolector_reserva'),
    
    # Otra ruta para mostrar órdenes para calificar recolector en reserva
    path('mostrar_ordenes_calificar_ciudadano_reserva/', MostrarOrdenesCalificarCiudadanoReservaView.as_view(), name='mostrar_ordenes_calificar_ciudadano_reserva'),
    
    # Tomar orden
    path('tomar_orden/<int:pk>/', TomarOrdenView.as_view(), name='tomar_orden'),
    
    # Tomar reserva
    path('tomar_reserva/<int:pk>/', TomarReservaView.as_view(), name='tomar_reserva'),
    
    # Confirmar posición del recolector
    path('confirmacion_posicion_recolector', views.confirmacion_posicion_recolector, name='confirmacion_posicion_recolector'),
    
    # Registrar usuario
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    
    # Validar contraseña
    path('validacion_pass/', views.validacion_pass, name='validacion_pass'),

    # Página de Quiénes somos
    path('somos', views.somos, name='somos'),
    
    # Página de Video de reciclaje
    path('video', views.video_reciclaje, name='video'),
    
    # Listar usuarios
    path('listar', UserList.as_view(), name="list_user"),
    
    # Enviar correo
    path('enviar_c', views.enviar_correo_pass, name="enviar_c"),
    
    # Agregar una orden de reciclaje
    path('orden_reciclaje', views.agregar_orden_reciclaje, name="orden_reciclaje"),
    
    # Agregar una orden de reserva
    path('orden_reserva', views.agregar_orden_reserva, name="orden_reserva"),
    
    # Autenticar usuario
    path('autenticar_us', Autenticar_us.as_view(), name="autenticar_us"),
    
    # Mostrar clave primaria
    path('primarykey', views.key, name="primarykey"),
    
    # Mensaje de contraseña
    path('mensaje_pass', views.mensaje, name="mensaje_pass"),
    
    # Error de validación
    path('error_validacion', views.error_validacion, name='error_validacion'),
    
    # Confirmación 3
    path('confirmacion3', views.confirmacion3, name="confirmacion3"),
    
    # Confirmación 4
    path('confirmacion4', views.confirmacion4, name="confirmacion4"),
    
    # Ver orden de reciclaje
    path('verOrdenReciclaje', OrdenList.as_view(), name="verOrdenReciclaje"),
    
    # Confirmación 2
    path('confirmacion2', views.confirmacion, name="confirmacion2"),
    
    # Listar órdenes de reserva
    path('reserva_list', Orden_Reserva_List.as_view(), name="reserva_list"),
    
    # Ver calificación de recolector por ciudadano
    path('verCalificacionRecolectorCiudadano', views.verCalificacionRecolectorCiudadano, name="verCalificacionRecolectorCiudadano"),
    
    # Ver calificación de reciclador
    path('verCalificacionReciclador', views.verCalificacionReciclador, name="verCalificacionReciclador"),
    
    # Ver registro de entrega de material
    path('verRegistroEntregaMaterial', views.verRegistroEntregaMaterial, name="verRegistroEntregaMaterial"),
    
    # Agregar calificación de reciclador
    path('agregar_calificacion_reciclador', views.agregar_calificacion_reciclador, name="agregar_calificacion_reciclador"),
    
    # Agregar registro de entrega de material
    path('agregar_registro_entrega_material', views.agregar_registro_entrega_material, name="agregar_registro_entrega_material"),
    
    # Editar usuario
    path('editar_user/<int:pk>/', views.UserUpdate.as_view(), name='editar_user'),
    
    # Editar calificación de recolector por ciudadano
    path('editar_calificacion_recolector_ciudadano/<int:calificacion_recolector_ciudadano_id>', views.editar_calificacion_recolector_ciudadano, name="editar_calificacion_recolector_ciudadano"),
    
    # Editar calificación de reciclador
    path('editar_calificacion_reciclador/<int:calificacion_reciclador_id>', views.editar_calificacion_reciclador, name="editar_calificacion_reciclador"),
    
    # Editar registro de entrega de material
    path('editar_registro_entrega_matrial/<int:registro_entrega_matrial_id>', views.editar_registro_entrega_matrial, name="editar_registro_entrega_matrial"),
    
    # Borrar usuario
    path('borrar_user/<int:pk>', UserDelete.as_view(), name="borrar_user"),
    
    # Actualizar orden
    path('actualizar_orden/<int:pk>', ActualizarOrden.as_view(), name="actualizar_orden"),
    
    # Actualizar reserva
    path('actualizar_reserva/<int:pk>', ActualizarReserva.as_view(), name="actualizar_reserva"),
    
    # Borrar calificación de recolector por ciudadano
    path('borrar_calificacion_recolector_ciudadano/<int:calificacion_recolector_ciudadano_id>', views.borrar_calificacion_recolector_ciudadano, name="borrar_calificacion_recolector_ciudadano"),
    
    # Borrar calificación de reciclador
    path('borrar_calificacion_reciclador/<int:calificacion_reciclador_id>', views.borrar_calificacion_reciclador, name="borrar_calificacion_reciclador"),
    
    # Borrar registro de entrega de material
    path('borrar_registro_entrega_material/<int:registro_entrega_material_id>', views.borrar_registro_entrega_material, name="borrar_registro_entrega_material"),
]
