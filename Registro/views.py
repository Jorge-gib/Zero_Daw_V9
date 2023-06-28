from django.shortcuts import render
from .models import Reserva_orden, UserModelo, Calificacion_recolector_ciudadano, Orden_reciclaje, Calificacion_reciclador, Registro_entrega_material
from .forms import  OrdenConcluir, OrdenUpdateForm, Posicion_recolectorForm, PassUpdateForm, UserUpdateForm, Reserva_ordenForm, RegistroForm, Calificacion_recolector_ciudadanoForm, Calificacion_recicladorForm, Registro_entrega_materialForm, Orden_reciclajeForm
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

# Create your views here.
class UserDelete(DeleteView):
    model = UserModelo
    template_name = 'Registro/borrar_user.html'
    success_url = reverse_lazy('confirmacion3')

################################################

def agregar_calificacion_recolector_ciudadano(request, id_orden):
    if request.method == 'POST':
        form = Calificacion_recolector_ciudadanoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.id_orden = id_orden
            model_instance.save()
            return render(request, 'Registro/confirmacion_calificacion.html', {'form': form})
    else:
        form = Calificacion_recolector_ciudadanoForm()
    return render(request, 'Registro/agregar_calificacion_recolector_ciudadano.html', {'form': form})


class ActualizarOrden(UpdateView):
    model = Orden_reciclaje
    form_class = OrdenConcluir
    template_name = 'Registro/actualizar_orden.html'
    success_url = reverse_lazy('confirmacion4')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.object
        return context
##############################################    

UserModel = get_user_model()

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
            return render(self.request, 'Registro/primarykey.html', {'form': form})

        # Verificar si el usuario ya existe
        if UserModelo.objects.filter(username=username).exists():
            form.add_error('username', 'El usuario ya existe')
            return render(self.request, 'Registro/us.html', {'form': form})

        # Guardar el objeto UserModelo
        self.object = form.save()

        return super().form_valid(form)

def key(request):
    context={}
    return render(request, 'Registro/primarykey.html', context)
def mensaje(request):
    context={}
    return render(request, 'Registro/mensaje_pass_exitoso.html', context)
def somos(request):
    context={}
    return render(request, 'Usuario/somos.html', context)
def error_validacion(request):
    context={}
    return render(request, 'Registro/error_validacion.html', context)

def enviar_correo_pass(request):
    context={}
    return render(request, 'Registro/recuperar_pass.html', context)
 
class Autenticar_us(ListView):
    model = UserModelo
    template_name = 'Registro/autenticar_us.html'

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
#############

# Create your views here.

       
def registro(request):
    context={}
    return render(request, 'home.html', context)

def confirmacion(request):
    context={}
    return render(request, 'Registro/confirmacion_2.html', context)

def confirmacion_posicion_recolector(request):
    context={}
    return render(request, 'Registro/confirmacion_posicion_recolector.html', context)

def confirmacion3(request):
    context={}
    return render(request, 'Registro/confirmacion_3.html', context)

def confirmacion4(request):
    context={}
    return render(request, 'Registro/confirmacion_4.html', context)








def verCalificacionRecolectorCiudadano(request):
    calificacion_recolector_ciudadano = Calificacion_recolector_ciudadano.objects.all()
    return render(request, "Pagina/ver_calificacion_recolector_ciudadano.html", {'calificacion_recolector_ciudadano': calificacion_recolector_ciudadano})


def verCalificacionReciclador(request):
    calificacion_reciclador = Calificacion_reciclador.objects.all()
    return render(request, "Pagina/ver_calificacion_reciclador.html", {'calificacion_reciclador': calificacion_reciclador})

def verRegistroEntregaMaterial(request):
    registro_entrega_material = Registro_entrega_material.objects.all()
    return render(request, "Pagina/ver_registro_entrega_material.html", {'registro_entrega_material': registro_entrega_material})






class OrdenList(LoginRequiredMixin, ListView):
    model = Orden_reciclaje
    template_name = 'Registro/detalle.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrar los objetos de orden_reciclaje por el id del UserModelo logeado
        queryset = queryset.filter(id_user=self.request.user.id)
        return queryset

    
#####################################################################################################

class Orden_Reserva_List(LoginRequiredMixin, ListView):
    model = Reserva_orden
    template_name = 'Registro/detalle_reserva.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrar los objetos de orden_reciclaje por el id del UserModelo logeado
        queryset = queryset.filter(id_user=self.request.user.id)
        return queryset
####################################################################################################
class TomarOrdenView(UpdateView):
    model = Orden_reciclaje
    form_class = OrdenUpdateForm
    template_name = 'Registro/tomar_orden.html'
    success_url = reverse_lazy('confirmacion_posicion_recolector')

    

###############################################################################################################

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

#################################################################################################################




#########################################################################################################################


def agregar_calificacion_reciclador(request):
    if request.method == "POST":
        form = Calificacion_recicladorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_calificacion_reciclador")
    else:
        form = Calificacion_recicladorForm()
        return render(request, "Pagina/agregar_calificacion_reciclador.html", {'form': form})
    
##########################################################################################################################

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



############################################################################################################################

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

def borrar_user(request, user_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = User.objects.get(id=user_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('list_user')

#################################################################################################################################




#################################################################################################################################





##################################################################################################################################





################################################################################################################################





################################################################################################################################





####################################################################################################################################


def borrar_calificacion_recolector_ciudadano(request, calificacion_recolector_ciudadano_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Calificacion_recolector_ciudadano.objects.get(id=calificacion_recolector_ciudadano_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('verCalificacionRecolectorCiudadano')


####################################################################################################################################

def borrar_calificacion_reciclador(request, calificacion_reciclador_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Calificacion_reciclador.objects.get(id=calificacion_reciclador_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('verCalificacionReciclador')


###################################################################################################################################

def borrar_registro_entrega_material(request, registro_entrega_material_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Registro_entrega_material.objects.get(id=registro_entrega_material_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('verRegistroEntregaMaterial')


#####################################################################################################################################


def borrar_orden_reciclaje(request, orden_reciclaje_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Orden_reciclaje.objects.get(id=orden_reciclaje_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('verOrdenReciclaje')

#####################################################################################################################################




class UserUpdate(UpdateView):
    model = UserModelo
    form_class = UserUpdateForm
    template_name = 'Registro/editar_user.html'
    success_url = reverse_lazy('confirmacion2')





#####################################################################################################################################




##########################################################################################################################




#################################################################################################################################



################################################################################################################################




#################################################################################################################################





#######################################################################################################################




#######################################################################################################################


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


def editar_calificacion_reciclador(request, calificacion_reciclador_id):
    # Recuperamos la instancia de la carrera
    instancia = Calificacion_reciclador.objects.get(id=calificacion_reciclador_id)

    # Creamos el formulario con los datos de la instancia
    form = Calificacion_recicladorForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = Calificacion_recicladorForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Pagina/calificacion_reciclador.html", {'form': form})


######################################################################################################################



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






