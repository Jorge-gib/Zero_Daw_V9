from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from django.http import HttpResponseRedirect
import datetime
from django.http import Http404
from .forms import  Registro_pago_reservaForm, Registro_pagoForm, ResepcionDesechosReservaForms, ResepcionDesechosForms, Calificacion_recolector_reservaForm, ReservaConcluir, ReservaUpdateForm, Calificacion_ciudadanoForm, Calificacion_recolectorForm, OrdenConcluir, OrdenUpdateForm, Posicion_recolectorForm, PassUpdateForm, UserUpdateForm, Reserva_ordenForm, RegistroForm, Calificacion_recolector_ciudadanoForm, Registro_entrega_materialForm, Orden_reciclajeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy 
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import redirect
import os

# Clase para borrar un usuario
class UserDelete(DeleteView):
    model = UserModelo
    template_name = 'Registro/borrar_user.html'
    success_url = reverse_lazy('confirmacion3')

################################################
# funcion para redirigir confirmacion calificacion
def confirmar_comentario(request):
    context={}
    return render(request, 'Registro/confirmacion_calificacion.html', context)

# funcion para agregar calificacion de un recolector a un cudadano
def agregar_calificacion_recolector_ciudadano(request, id_orden):
    if request.method == 'POST':
        calificacion = Calificacion_recolector_ciudadano()
        calificacion.id_orden_id = id_orden
        calificacion.calificacion_estrellas_ciudadano = request.POST['calificacion_estrellas_ciudadano']
        calificacion.opinion_servicio_ciudadano = request.POST['opinion_servicio_ciudadano']
        calificacion.save()
        return render(request, 'Registro/confirmacion_calificacion.html', {'calificacion': calificacion})
    else:
        form = Calificacion_recolectorForm()
    orden = Orden_reciclaje.objects.get(id_orden=id_orden)
    return render(request, 'Registro/agregar_calificacion_recolector_ciudadano.html', {'form': form, 'orden': orden})

###########################################



# funcion para agregar calificacion de un recolector a un cudadano por reserva
def agregar_calificacion_ciudadano_reserva(request, id_orden):
    if request.method == 'POST':
        calificacion = Calificacion_recolector_ciudadano_reserva()
        calificacion.id_orden_id = id_orden
        calificacion.calificacion_estrellas_ciudadano = request.POST['calificacion_estrellas_ciudadano']
        calificacion.opinion_servicio_ciudadano = request.POST['opinion_servicio_ciudadano']
        calificacion.save()
        return render(request, 'Registro/confirmacion_calificacion.html', {'calificacion': calificacion})
    else:
        form = Calificacion_ciudadanoForm()
    orden = Reserva_orden.objects.get(id_orden=id_orden)
    return render(request, 'Registro/agregar_calificacion_ciudadano_reserva.html', {'form': form, 'orden': orden})

###########################################



# Agegrar calificacion de un ciudadano a recoletor

def agregar_calificacion_recolector_ciudadano2(request, id_orden):
    orden = Orden_reciclaje.objects.get(id_orden=id_orden)
    
    try:
        calificacion = Calificacion_recolector_ciudadano.objects.get(id_orden_id=id_orden)
    except Calificacion_recolector_ciudadano.DoesNotExist:
        calificacion = Calificacion_recolector_ciudadano(id_orden_id=id_orden)

    if request.method == 'POST':
        form = Calificacion_ciudadanoForm(request.POST, instance=calificacion)  # Agregar 'instance=calificacion' aquí
        if form.is_valid():
            form.save()
            return render(request, 'Registro/confirmacion_calificacion.html', {'calificacion': calificacion})
        else:
            return render(request, 'Registro/agregar_calificacion_recolector_ciudadano2.html', {'form': form, 'orden': orden})
    else:
        form = Calificacion_ciudadanoForm(instance=calificacion)
        return render(request, 'Registro/agregar_calificacion_recolector_ciudadano2.html', {'form': form, 'orden': orden})
    
    
# Agregar calificacion de un ciudadano a recolestor por reserva
def agregar_calificacion_recolector_reserva(request, id_orden):
    orden = Reserva_orden.objects.get(id_orden=id_orden)
    
    try:
        calificacion = Calificacion_recolector_ciudadano_reserva.objects.get(id_orden_id=id_orden)
    except Calificacion_recolector_ciudadano.DoesNotExist:
        calificacion = Calificacion_recolector_ciudadano_reserva(id_orden_id=id_orden)

    if request.method == 'POST':
        form = Calificacion_recolector_reservaForm(request.POST, instance=calificacion)  # Agregar 'instance=calificacion' aquí
        if form.is_valid():
            form.save()
            return render(request, 'Registro/confirmacion_calificacion.html', {'calificacion': calificacion})
        else:
            return render(request, 'Registro/agregar_calificacion_recolector_ciudadano3.html', {'form': form, 'orden': orden})
    else:
        form = Calificacion_recolector_reservaForm(instance=calificacion)
        return render(request, 'Registro/agregar_calificacion_recolector_ciudadano3.html', {'form': form, 'orden': orden})



#Actualiza la orden de reciclaje

class ActualizarOrden(UpdateView):
    model = Orden_reciclaje
    form_class = OrdenConcluir
    template_name = 'Registro/actualizar_orden.html'

    def get_success_url(self):
        return reverse_lazy('agregar_calificacion_recolector_ciudadano', kwargs={'id_orden': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.object
        return context

##############################################  
#Actualiza la orden de reciclaje reserva
class ActualizarReserva(UpdateView):
    model = Reserva_orden
    form_class = ReservaConcluir
    template_name = 'Registro/actualizar_reserva.html'

    def get_success_url(self):
        return reverse_lazy('agregar_calificacion_ciudadano_reserva', kwargs={'id_orden': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.object
        return context

##############################################    

UserModel = get_user_model()
# Funcon para actualizar password
def validacion_pass(request):
    if request.method == 'POST':
        form = PassUpdateForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            segundo_nombre_madre = form.cleaned_data['segundo_nombre_madre']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']

            try:
                user = UserModelo.objects.get(rut=rut, segundo_nombre_madre=segundo_nombre_madre)
            except UserModelo.DoesNotExist:
                return redirect('error_validacion')

            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                return redirect('mensaje_pass')
            else:
                # Las contraseñas no coinciden, mostrar mensaje de error
                return redirect('error_validacion')

    else:
        form = PassUpdateForm()

    context = {'form': form}
    return render(request, 'Registro/recuperar_pass.html', context)
    
    
################################################


  
# funcion para crear un usuario

class RegistroUsuario(CreateView):
    model = UserModelo
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        rut = form.cleaned_data.get('rut')
        username = form.cleaned_data.get('username')

        # Verificar si el rut ya está registrado
        if UserModelo.objects.filter(rut=rut).exists():
            form.add_error('rut', 'El rut ya está registrado')
            return self.form_invalid(form)

        # Verificar si el usuario ya existe
        if UserModelo.objects.filter(username=username).exists():
            form.add_error('username', 'El usuario ya existe')
            return self.form_invalid(form)

        # Guardar el objeto UserModelo
        self.object = form.save()

        # Obtener la instancia de la imagen cargada
        imagen_licencia = form.cleaned_data.get('licencia_automotriz')

        # Guardar la imagen en la carpeta 'licencias'
        if imagen_licencia:
            fs = FileSystemStorage(location=settings.CV_UPLOAD_PATH)
            nombre_archivo = os.path.basename(imagen_licencia.name)
            fs.save(nombre_archivo, imagen_licencia)

        return super().form_valid(form)

    def form_invalid(self, form):
        error_messages = []
        for field, errors in form.errors.items():
            field_label = form.fields[field].label
            error_messages.append(f"{field_label}: {', '.join(errors)}")
        error_message = 'Por favor, corrija los siguientes errores: {}'.format(' - '.join(error_messages))
        messages.error(self.request, error_message)
        return self.render_to_response(self.get_context_data(form=form))
# funcion para redireccionar en caso de que el rut que se ingrese ya exista
def key(request):
    context={}
    return render(request, 'Registro/primarykey.html', context)

#funcion para redireccionar en caso de que el cambio de clave sea exitoso
def mensaje(request):
    context={}
    return render(request, 'Registro/mensaje_pass_exitoso.html', context)
#Funcion para redireccionar a la presentacion de la organizacion
def somos(request):
    context={}
    return render(request, 'Usuario/somos.html', context)

#Funcion para llevar a la explicacion del mundo de reciclaje
def video_reciclaje(request):
    context={}
    return render(request, 'Registro/video.html', context)
#Funcion que lleva a la pagina del logo
def zero_daw(request):
    context={}
    return render(request, 'Registro/zero_daw.html', context)
# funcion que lleva a error de validacion
def error_validacion(request):
    context={}
    return render(request, 'Registro/error_validacion.html', context)
# funcion que lleva a la pagina de recuperacion de pass
def enviar_correo_pass(request):
    context={}
    return render(request, 'Registro/recuperar_pass.html', context)
 # clase para validar usuario
class Autenticar_us(ListView):
    model = UserModelo
    template_name = 'Registro/autenticar_us.html'
#funcion para listar usuarios
class UserList(ListView):
    model = UserModelo
    template_name = 'Usuario/list_user.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user  # Obtener el usuario actualmente autenticado

        # Verificar si el UserModelo existe para el rut del usuario autenticado
        if UserModelo.objects.filter(rut=user.rut).exists():
            # Filtrar los datos por el rut del usuario autenticado
            queryset = queryset.filter(rut=user.rut)
        else:
            return redirect(reverse_lazy('autenticar_us'))

        return queryset


# funcion de redireccionaiento a home
def registro(request):
    context={}
    return render(request, 'home.html', context)
#Funcion de redireccionamiento a confirmacion de perfil actualizado con exito
def confirmacion(request):
    context={}
    return render(request, 'Registro/confirmacion_2.html', context)
# funcion que redirecciona a confirmacion posicion recoletor
def confirmacion_posicion_recolector(request):
    context={}
    return render(request, 'Registro/confirmacion_posicion_recolector.html', context)
# conformacion de elemimnacion de cuenta
def confirmacion3(request):
    context={}
    return render(request, 'Registro/confirmacion_3.html', context)
# Conclusion de la orden
def confirmacion4(request):
    context={}
    return render(request, 'Registro/confirmacion_4.html', context)







# Ver calificacion recoletor
def verCalificacionRecolectorCiudadano(request):
    calificacion_recolector_ciudadano = Calificacion_recolector_ciudadano.objects.all()
    return render(request, "Pagina/ver_calificacion_recolector_ciudadano.html", {'calificacion_recolector_ciudadano': calificacion_recolector_ciudadano})


# Funcion para ver registro material
def verRegistroEntregaMaterial(request):
    registro_entrega_material = Registro_entrega_material.objects.all()
    return render(request, "Pagina/ver_registro_entrega_material.html", {'registro_entrega_material': registro_entrega_material})





#Listar todo en ordenes de reciclaje
class OrdenList(LoginRequiredMixin, ListView):
    model = Orden_reciclaje
    template_name = 'Registro/detalle.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrar los objetos de orden_reciclaje por el id del UserModelo logeado
        queryset = queryset.filter(id_user=self.request.user.id)
        return queryset

    
#####################################################################################################
#Listar todo en ordenes de reciclaje reserva
class Orden_Reserva_List(LoginRequiredMixin, ListView):
    model = Reserva_orden
    template_name = 'Registro/detalle_reserva.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrar los objetos de orden_reciclaje por el id del UserModelo logeado
        queryset = queryset.filter(id_user=self.request.user.id)
        return queryset
####################################################################################################
# Actualiza la orden
class TomarOrdenView(UpdateView):
    model = Orden_reciclaje
    form_class = OrdenUpdateForm
    template_name = 'Registro/tomar_orden.html'
    success_url = reverse_lazy('confirmacion_posicion_recolector')

    def form_valid(self, form):
        # Obtener la instancia del formulario pero no guardar aún
        orden_reciclaje = form.save(commit=False)
        
        # Asignar el rut del usuario actual al campo rut_recolector
        orden_reciclaje.rut_recolector = self.request.user.rut
        
        # Guardar la instancia del formulario
        orden_reciclaje.save()
        
        return super().form_valid(form)

###############################################################################################################
#Actualiza la reserva
class TomarReservaView(UpdateView):
    model = Reserva_orden
    form_class = ReservaUpdateForm
    template_name = 'Registro/tomar_reserva.html'
    success_url = reverse_lazy('confirmacion_posicion_recolector')

    def form_valid(self, form):
        # Obtener la instancia del formulario pero no guardar aún
        reserva_orden = form.save(commit=False)
        
        # Asignar el rut del usuario actual al campo rut_recolector
        reserva_orden.rut_recolector = self.request.user.rut
        
        # Guardar la instancia del formulario
        reserva_orden.save()
        
        return super().form_valid(form)

    

###############################################################################################################

# Actualiza reserva
class MostrarOrdenesView(ListView):
    model = UserModelo
    template_name = 'Registro/mostrar_ordenes.html'

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        url = reverse('tomar_orden', args=[orden_id])
        return redirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = Orden_reciclaje.objects.all()
        return context

###########################################################################################################
#Mostrar las reservas
class MostrarReservaView(ListView):
    model = UserModelo
    template_name = 'Registro/mostrar_reserva.html'

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        url = reverse('tomar_reserva', args=[orden_id])
        return redirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = Reserva_orden.objects.all()
        return context

###########################################################################################################
# Muestras las ordenes para ser actualizadas
class MostrarOrdenesParaEliminarView(ListView):
    model = UserModelo
    template_name = 'Registro/mostrar_ordenes_para_eliminar.html'

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        url = reverse_lazy('actualizar_orden', args=[orden_id])
        return redirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = Orden_reciclaje.objects.all()
        return context
    
#######################################################################################
# Muestra reservas a actualzar
class MostrarReservaParaEliminarView(ListView):
    model = UserModelo
    template_name = 'Registro/mostrar_reserva_para_eliminar.html'

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        url = reverse_lazy('agregar_calificacion_ciudadano_reserva', args=[orden_id])
        return redirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = Reserva_orden.objects.all()
        return context
    
#######################################################################################

#Mostrar ordenes calificar recolector
class MostrarOrdenesCalificarRecolectorView(LoginRequiredMixin, ListView):
    model = UserModelo
    template_name = 'Registro/mostrar_ordenes_para_calificar_recolector.html'
    login_url = '/login/'  # Define la URL de inicio de sesión si el usuario no está autenticado

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        url = reverse_lazy('agregar_calificacion_recolector_ciudadano2', args=[orden_id])
        
        # Actualizar el atributo 'estado' del modelo
        orden = Orden_reciclaje.objects.get(id_orden=orden_id)
        orden.estado = 'Calificado'
        orden.save()
        
        return redirect(url)

    def get_queryset(self):
        # Obtiene el ID del usuario actual
        id_user = self.request.user.id
        # Filtra las órdenes por el ID del usuario actual
        queryset = Orden_reciclaje.objects.filter(id_user_id=id_user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega las órdenes filtradas al contexto con el nombre 'ordenes'
        context['ordenes'] = self.get_queryset()
        return context

###############################################################################################################3
#mostrar reservas para calificar recolector
class MostrarOrdenesCalificarRecolectorReservaView(LoginRequiredMixin, ListView):
    model = UserModelo
    template_name = 'Registro/mostrar_para_finalizar_calificacion.html'
    login_url = '/login/'  # Define la URL de inicio de sesión si el usuario no está autenticado

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        url = reverse_lazy('agregar_calificacion_recolector_reserva', args=[orden_id])
        
        # Actualizar el atributo 'estado' del modelo
        orden = Reserva_orden.objects.get(id_orden=orden_id)
        orden.estado = 'Calificado'
        orden.save()
        
        return redirect(url)

    def get_queryset(self):
        # Obtiene el ID del usuario actual
        id_user = self.request.user.id
        # Filtra las órdenes por el ID del usuario actual
        queryset = Reserva_orden.objects.filter(id_user_id=id_user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega las órdenes filtradas al contexto con el nombre 'ordenes'
        context['ordenes'] = self.get_queryset()
        return context





##################################################################################################################
# Mosrar ordenes oara calificar al ciudadano por reserva
class MostrarOrdenesCalificarCiudadanoReservaView(ListView):
    model = UserModelo
    template_name = 'Registro/mostrar_ordenes_para_calificar_recolector_reserva.html'

    def post(self, request, *args, **kwargs):
        orden_id = request.POST.get('orden_id')
        url = reverse_lazy('agregar_calificacion_ciudadano_reserva', args=[orden_id])
        
        # Actualizar el atributo 'estado' del modelo
        orden = Reserva_orden.objects.get(id_orden=orden_id)
        orden.estado = 'Calificado'
        orden.save()
        
        return redirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = Reserva_orden.objects.all()
        return context


#################################################################################################################


    
##########################################################################################################################
# funcion para agregar registro entrega material
def agregar_registro_entrega_material(request):
    if request.method == "POST":
        form = Registro_entrega_materialForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_registro_entrega_material")
    else:
        form = Registro_entrega_materialForm()
        return render(request, "Pagina/agregar_registro_entrega_material.html", {'form': form})
    


############################################################################################################################
# Funcion para realizar una orden de reciclaje
def agregar_orden_reciclaje(request):
    if request.method == 'POST':
        form = Orden_reciclajeForm(request.POST)
        
        
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return render(request, 'Registro/confirmacion_1.html', {'form': form})
            
       
    else:
        form = Orden_reciclajeForm()
    return render(request, 'Registro/orden_reciclaje.html', {'form': form})

#############################################
# Realizar reserva
def agregar_orden_reserva(request):
    if request.method == 'POST':
        form = Reserva_ordenForm(request.POST)
        
        
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return render(request, 'Registro/confirmacion_1.html', {'form': form})
            
       
    else:
        form = Reserva_ordenForm()
    return render(request, 'Registro/reserva.html', {'form': form})

##############################################################################################################################
# Funcion que borra un ususario
def borrar_user(request, user_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = User.objects.get(id=user_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('list_user')

#################################################################################################################################

#funcion eliminada
def borrar_calificacion_recolector_ciudadano(request, calificacion_recolector_ciudadano_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Calificacion_recolector_ciudadano.objects.get(id=calificacion_recolector_ciudadano_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('verCalificacionRecolectorCiudadano')


####################################################################################################################################


###################################################################################################################################
#funcion eliminada
def borrar_registro_entrega_material(request, registro_entrega_material_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Registro_entrega_material.objects.get(id=registro_entrega_material_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('verRegistroEntregaMaterial')


#####################################################################################################################################

#Funcion eliminada
def borrar_orden_reciclaje(request, orden_reciclaje_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Orden_reciclaje.objects.get(id=orden_reciclaje_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('verOrdenReciclaje')

#####################################################################################################################################



#Funcion para actualizar los datos del usuario
class UserUpdate(UpdateView):
    model = UserModelo
    form_class = UserUpdateForm
    template_name = 'Registro/editar_user.html'
    success_url = reverse_lazy('confirmacion2')





#####################################################################################################################################


#Funcion eliminada
def editar_calificacion_recolector_ciudadano(request, calificacion_recolector_ciudadano_id):
    # Recuperamos la instancia de la carrera
    instancia = Calificacion_recolector_ciudadano.objects.get(id=calificacion_recolector_ciudadano_id)

    # Creamos el formulario con los datos de la instancia
    form = Calificacion_recolector_ciudadanoForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = Calificacion_recolector_ciudadanoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Pagina/calificacion_recolector_ciudadano.html", {'form': form})


############################################################################################################################

# Funcion eliminada



######################################################################################################################


# Funcion eliminada
def editar_registro_entrega_matrial(request, registro_entrega_material_id):
    # Recuperamos la instancia de la carrera
    instancia = Registro_entrega_material.objects.get(id=registro_entrega_material_id)

    # Creamos el formulario con los datos de la instancia
    form = Registro_entrega_materialForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = Registro_entrega_materialForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Pagina/registro_entrega_material.html", {'form': form})


#########################################################################################################################

#funcion eliminada
def editar_orden_reciclaje(request, orden_reciclaje_id):
    # Recuperamos la instancia de la carrera
    instancia = Orden_reciclaje.objects.get(id=orden_reciclaje_id)

    # Creamos el formulario con los datos de la instancia
    form = Orden_reciclajeForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = Orden_reciclajeForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Pagina/orden_reciclaje.html", {'form': form})
########################################################
#######################################################################################
# Muestra los registros de recicladores
class MostrarResepciones(ListView):
    model = Recepcion_desechos
    template_name = 'Registro/ver_recicladores.html'
    context_object_name = 'registros'

    def get_queryset(self):
        # Filtrar los registros de recepción de desechos por la comuna del usuario
        comuna_usuario = self.request.user.comuna
        queryset = Recepcion_desechos.objects.filter(id_orden__id_user__comuna=comuna_usuario)
        return queryset
    
#######################################################################################
class MostrarResepcionesReserva(ListView):
    model = Recepcion_desechos
    template_name = 'Registro/ver_recicladores_reserva.html'
    context_object_name = 'registros'

    def get_queryset(self):
        # Filtrar los registros de recepción de desechos por la comuna del usuario
        comuna_usuario = self.request.user.comuna
        queryset = Recepcion_desechos.objects.filter(id_orden__id_user__comuna=comuna_usuario)
        return queryset
    
########################################################################################

    
#######################################################################################

## Vista para mostrtar recolectores
class MostrarRecolectores(LoginRequiredMixin, ListView):
    model = UserModelo
    template_name = 'Registro/ver_recolectores.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        # Obtenemos la comuna del usuario actual
        comuna_usuario_actual = self.request.user.comuna
        
        # Filtramos los usuarios que son recolectores y están en la misma comuna del usuario actual
        queryset = UserModelo.objects.filter(tipo_usuario='Recolector', comuna=comuna_usuario_actual)
        
        return queryset

    def get(self, request, *args, **kwargs):
        # Si se ha seleccionado un usuario
        if 'id_user' in request.GET:
            id_user = request.GET['id_user']
            # Redirigir a la URL 'autorizar_o_denegar' con el id_user como parámetro
            return redirect(reverse_lazy('actualizar_recolector/', kwargs={'pk': id_user}))

        return super().get(request, *args, **kwargs)


##################################################################

## Actualizar campo validar usuario para dar autorizacion al recolector


################################
def actualizar_recolector(request, id_user):
    if request.method == 'GET':
        # Aquí manejas la lógica para mostrar la confirmación de validación
        # Puedes obtener el usuario usando el id pasado en la URL
        usuario = get_object_or_404(UserModelo, id=id_user)
        return render(request, 'Registro/autorizar_recolector.html', {'usuario': usuario})
    elif request.method == 'POST':
        # Obtener el usuario y actualizar el campo validacion_recolector a True
        usuario = get_object_or_404(UserModelo, id=id_user)
        usuario.validacion_recolector = True
        usuario.save()
        # Redireccionar a la página de confirmación de validación o a donde corresponda
        return redirect(reverse('confirmacion_validacion'))
    
## Pagina de rechazo a recolerctor
def rechazar(request):
    context={}
    return render(request, 'Registro/rechazar.html', context)
# Pagina de asepto a recolerctor
def confirmacion_validacion(request):
    context={}
    return render(request, 'Registro/confirmacion_validacion.html', context)

#######################################################################################
## Vista para mostrtar ordenes de reciclaje para resepcionar desechos

class MostrarOrdenesResepcionar(LoginRequiredMixin, ListView):
    model = Orden_reciclaje
    template_name = 'Registro/mostrar_ordenes_para_resepcionar.html'
    context_object_name = 'ordenes'

    def post(self, request, *args, **kwargs):
        id_orden = request.POST.get('id_orden')
        if id_orden:
            # Obtener la orden de reciclaje
            

            # Redirigir a la URL 'hacer_resepcion_desechos' con el id_orden como parámetro
            return redirect(reverse_lazy('hacer_resepcion_desechos', kwargs={'pk': id_orden}))

        # Si no se ha enviado un id_orden, continuar con la vista actual
        return super().get(request, *args, **kwargs)

##########################################################################################
## Vista para mostrtar ordenes de reciclaje para resepcionar desechos

##################################################################
#Hacer una recepcion de desechos
def HacerResepcionDesechosView(request, id_orden):
    # Lógica para obtener la orden con el id proporcionado
    orden = Orden_reciclaje.objects.get(id_orden=id_orden)
    id_orden = orden.id_orden
    # Actualizar el campo estado a "Expirado"
    orden.estado = "Expirado"
    orden.save()

    if request.method == 'POST':
        form = ResepcionDesechosForms(request.POST)
        
        if form.is_valid():
            # Guardar la información en el modelo Recepcion_desechos
            recepcion = form.save(commit=False)
            recepcion.id_orden = orden
            recepcion.save()

            # Obtener el id_registro de la recepción guardada
            id_registro = recepcion.id_registro

            # Redirigir a la confirmación con el id_registro
            return redirect(reverse_lazy('pago_recolector', kwargs={'id_registro': id_registro, 'id_orden': id_orden}))
            
    else:
        form = Reserva_ordenForm()
    return render(request, 'Registro/hacer_resepcion_desechos.html', {'form': form, 'orden_id': id_orden})
#########################################################################

class MostrarOrdenesResepcionarReserva(LoginRequiredMixin, ListView):
    model = Reserva_orden
    template_name = 'Registro/mostrar_ordenes_para_resepcionar_reserva.html'
    context_object_name = 'ordenes'

    def post(self, request, *args, **kwargs):
        id_orden = request.POST.get('id_orden')
        if id_orden:
            # Obtener la orden de reciclaje
            

            # Redirigir a la URL 'hacer_resepcion_desechos' con el id_orden como parámetro
            return redirect(reverse_lazy('hacer_resepcion_desechos_reserva', kwargs={'pk': id_orden}))

        # Si no se ha enviado un id_orden, continuar con la vista actual
        return super().get(request, *args, **kwargs)
##############################################################################

def HacerRecepcionDesechosReservaView(request, id_orden):
    # Lógica para obtener la orden con el id proporcionado
  
    orden = Reserva_orden.objects.get(id_orden=id_orden)
    id_orden = orden.id_orden
    # Actualizar el campo estado a "Expirado"
    orden.estado = "Expirado"
    orden.save()

    if request.method == 'POST':
        form = ResepcionDesechosReservaForms(request.POST)
        
        if form.is_valid():
            # Guardar la información en el modelo Recepcion_desechos_reserva
            fecha_registro = form.cleaned_data['fecha_registro']
            cantidad_plastico = form.cleaned_data['cantidad_plastico']
            cantidad_vidrio = form.cleaned_data['cantidad_vidrio']
            cantidad_carton = form.cleaned_data['cantidad_carton']
            cantidad_aluminio = form.cleaned_data['cantidad_aluminio']
            cantidad_metal = form.cleaned_data['cantidad_metal']
            cantidad_electrodomesticos = form.cleaned_data['cantidad_electrodomesticos']
            
            recepcion = Recepcion_desechos_reserva.objects.create(
                id_orden=orden,  # Usando el objeto orden en lugar del ID
                fecha_registro=fecha_registro,
                cantidad_plastico=cantidad_plastico,
                cantidad_vidrio=cantidad_vidrio,
                cantidad_carton=cantidad_carton,
                cantidad_aluminio=cantidad_aluminio,
                cantidad_metal=cantidad_metal,
                cantidad_electrodomesticos=cantidad_electrodomesticos
            )
            recepcion.save()
            id_registro = recepcion.id_registro

            # Redirigir a la confirmación
            return redirect(reverse_lazy('pago_recolector_reserva', kwargs={'id_registro': id_registro, 'id_orden': id_orden}))
            
    else:
        form = ResepcionDesechosReservaForms()
    return render(request, 'Registro/hacer_resepcion_desechos_reserva.html', {'form': form, 'orden_id': id_orden})

def CalculoPagoView(request, id_registro, id_orden):
    try:
        recepcion = Recepcion_desechos.objects.get(id_registro=id_registro)
        orden = recepcion.id_registro
        orden_id = recepcion.id_registro
        orden_reciclaje = Orden_reciclaje.objects.get(id_orden=id_orden)
    except Recepcion_desechos.DoesNotExist:
        raise Http404("La recepción de desechos no existe")
    except Orden_reciclaje.DoesNotExist:
        raise Http404("La orden de reciclaje asociada no existe")

    total_residuos = sum([
        getattr(recepcion, f'cantidad_{material}') for material in ['plastico', 'vidrio', 'carton', 'aluminio', 'metal', 'electrodomesticos']
    ])

    precio_plastico = 50
    precio_vidrio = 200
    precio_carton = 300
    precio_aluminio = 700
    precio_metal = 700
    precio_electrodomesticos = 2000

    costo_total = (recepcion.cantidad_plastico * precio_plastico) + \
                  (recepcion.cantidad_vidrio * precio_vidrio) + \
                  (recepcion.cantidad_carton * precio_carton) + \
                  (recepcion.cantidad_aluminio * precio_aluminio) + \
                  (recepcion.cantidad_metal * precio_metal) + \
                  (recepcion.cantidad_electrodomesticos * precio_electrodomesticos)

    # Obtener el número de teléfono del usuario autenticado
    numero_telefono_usuario = request.user.telefono
    
    # Obtener el rut_recolector de la orden
    rut_recolector = orden_reciclaje.rut_recolector

    if request.method == 'POST':
        url = reverse('registrar_pago', kwargs={'orden': orden, 'numero_telefono_usuario': numero_telefono_usuario, 'total_residuos': total_residuos, 'costo_total': costo_total})
        return redirect(url)

    return render(request, 'Registro/calculo_pago.html', {'costo_total': costo_total, 'total_residuos': total_residuos, 'orden': orden_reciclaje, 'numero_telefono_usuario': numero_telefono_usuario, 'rut_recolector': rut_recolector})
###########################################
def CalculoPagoReservaView(request, id_registro, id_orden):
    try:
        recepcion = Recepcion_desechos_reserva.objects.get(id_registro=id_registro)
        orden = recepcion.id_registro
        orden_reciclaje = Reserva_orden.objects.get(id_orden=id_orden)
    except Recepcion_desechos_reserva.DoesNotExist:
        raise Http404("La recepción de desechos no existe")
    except Reserva_orden.DoesNotExist:
        raise Http404("La orden de reciclaje asociada no existe")

    total_residuos = sum([
        getattr(recepcion, f'cantidad_{material}') for material in ['plastico', 'vidrio', 'carton', 'aluminio', 'metal', 'electrodomesticos']
    ])

    precio_plastico = 50
    precio_vidrio = 200
    precio_carton = 300
    precio_aluminio = 700
    precio_metal = 700
    precio_electrodomesticos = 2000

    costo_total = (recepcion.cantidad_plastico * precio_plastico) + \
                  (recepcion.cantidad_vidrio * precio_vidrio) + \
                  (recepcion.cantidad_carton * precio_carton) + \
                  (recepcion.cantidad_aluminio * precio_aluminio) + \
                  (recepcion.cantidad_metal * precio_metal) + \
                  (recepcion.cantidad_electrodomesticos * precio_electrodomesticos)

     # Obtener el número de teléfono del usuario autenticado
    numero_telefono_usuario = request.user.telefono
    
    # Obtener el rut_recolector de la orden
    rut_recolector = orden_reciclaje.rut_recolector

    

    if request.method == 'POST':
        url = reverse('registrar_pago_reserva', kwargs={'orden': orden, 'numero_telefono_usuario': numero_telefono_usuario, 'total_residuos': total_residuos, 'costo_total': costo_total})
        return redirect(url)

    return render(request, 'Registro/calculo_pago_reserva.html', {'costo_total': costo_total, 'total_residuos': total_residuos, 'orden': orden_reciclaje, 'numero_telefono_usuario': numero_telefono_usuario, 'rut_recolector': rut_recolector})

###########################################


def AgregarPagoView(request, id_registro, numero_telefono_usuario, total_residuos, costo_total):
    registro_pago = Registro_pago.objects.create(
        id_registro_id=id_registro,
        fecha_pago=datetime.date.today(),
        telefono_reciclador = request.user.telefono,
        total_material_reciclado=total_residuos,
        monto_pago=costo_total
    )
    return redirect('pago_registrado')  # Redirige a la página deseada después de guardar

def PagoRegistradoView(request):
    context={}
    return render(request, 'Registro/confirmacion_pago.html', context)

############################################

def AgregarPagoReservaView(request, id_registro, numero_telefono_usuario, total_residuos, costo_total):
    registro_pago = Registro_pago_reserva.objects.create(
        id_registro_id=id_registro,
        fecha_pago=datetime.date.today(),
        telefono_reciclador = request.user.telefono,
        total_material_reciclado=total_residuos,
        monto_pago=costo_total
    )
    return redirect('pago_registrado')  # Redirige a la página deseada después de guardar
    
##################################################

class MostrarPromesasPago(ListView):
    model = Registro_pago
    template_name = 'Registro/ver_promesas_pago.html'
    context_object_name = 'promesas_pago'

    def get_queryset(self):
        # Obtener el usuario actual
        user = self.request.user
        # Obtener el rut del usuario que está ejecutando la vista
        rut_usuario = user.rut
        
        # Filtrar los registros de pago por el rut del usuario
        queryset = Registro_pago.objects.filter(
            id_registro__id_orden__rut_recolector=rut_usuario
        )
        return queryset
    
##################################################

class MostrarPromesasPagoReserva(ListView):
    model = Registro_pago_reserva
    template_name = 'Registro/ver_promesas_pago_reserva.html'
    context_object_name = 'promesas_pago'

    def get_queryset(self):
        # Obtener el usuario actual
        user = self.request.user
        # Obtener el rut del usuario que está ejecutando la vista
        rut_usuario = user.rut
        
        # Filtrar los registros de pago por el rut del usuario
        queryset = Registro_pago_reserva.objects.filter(
            id_registro__id_orden__rut_recolector=rut_usuario
        )
        return queryset
    
################################################

class MyLoginView(LoginView):
    template_name = 'Usuario/login.html'

    def form_valid(self, form):
        # Recupera el usuario que está intentando iniciar sesión
        username = form.cleaned_data.get('username')
        user = UserModelo.objects.get(username=username)
        
        # Verifica si el usuario es un recolector y si el campo validacion_recolector es False
        if user.tipo_usuario == 'Recolector' and not user.validacion_recolector:
            return HttpResponseRedirect(reverse('acceso_denegado'))  # Redirige al usuario a la página de acceso_denegado
        
        return super().form_valid(form)
#######################################################

def AccesoDenegadoView(request):
    context={}
    return render(request, 'Usuario/acceso_denegado.html', context)