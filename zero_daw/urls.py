from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from Registro.views import MyLoginView


# Configuración de las URLs del proyecto academico

urlpatterns = [
    # Ruta para la administración de Django
    path('admin/', admin.site.urls),
    
    # Ruta para el mapeador local de la aplicación Registro
    path('registro/', include('Registro.urls')),
    
    # Ruta para el mapeador local de la aplicación Usuario
    
    # Inclusión de las URLs de la aplicación api
    path('api/', include('api.urls')),
    
    # Rutas para iniciar y cerrar sesión
    path('login', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    
    # Ruta de inicio, muestra la plantilla home.html
    path('', TemplateView.as_view(template_name='home.html'), name='home'),        
]
