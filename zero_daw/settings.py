from pathlib import Path
import os


# Construye rutas dentro del proyecto de esta manera: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de Django para archivos adjuntos
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CV_UPLOAD_DIR = 'licencias/'
CV_UPLOAD_PATH = os.path.join(MEDIA_ROOT, CV_UPLOAD_DIR)

# ADVERTENCIA DE SEGURIDAD: ¡mantén la clave secreta utilizada en producción en secreto!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-*u7&#g*6%cyj+a%+pvoovf&c357g&kc-165kh223*1ql_8digg')

# ADVERTENCIA DE SEGURIDAD: ¡no ejecutes con debug activado en producción!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = []

# Definición de aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'Registro',  # Aplicación de tu proyecto
    'api',
    'rest_framework',
    'pwa',
]

# Middleware utilizado en la aplicación
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL principal del proyecto
ROOT_URLCONF = 'zero_daw.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Aplicación WSGI para el proyecto
WSGI_APPLICATION = 'zero_daw.wsgi.application'

# Configuración de la base de datos

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/XE',
        'USER': 'ZERO_DAW_BD',
        'PASSWORD': 'jorge123',
        'OPTIONS': {
            'threaded': True,
        },
        'TEST': {
            'USER': 'default_test',
            'TBLSPACE': 'default_test_tbls',
            'TBLSPACE_TMP': 'default_test_tbls_tmp',
        },
    },

}



# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalización
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JavaScript, Imágenes)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'

# Tipo de campo de clave primaria predeterminado
AUTH_USER_MODEL = 'Registro.UserModelo'

# Redireccionamientos después del inicio de sesión/cierre de sesión
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


