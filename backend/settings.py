"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_PATH = os.path.join(BASE_DIR,'config.json')
if os.path.isfile(CONFIG_PATH):
    with open ( os.path.join(BASE_DIR,'config.json'),mode='r',encoding='utf-8' ) as conf:
        CONFIG = json.load(conf)
else:
    CONFIG = {}

def database_setting(environ_key, config_key, default_value):
    return os.environ.get(environ_key, CONFIG.get(config_key ,default_value))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('SECRET_KEY','')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
if 'DYNO' in os.environ:
    DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'v1',
    'django_celery',
    'django_celery_results',
    'rest_framework',
    'corsheaders',
    'drf_yasg'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE':   CONFIG.get('DB_ENGINE' ,'django.db.backends.postgresql_psycopg2'),
#         'NAME':     CONFIG.get('DB_NAME'   , 'postgres'),
#         'USER':     CONFIG.get('DB_USERNAME' ,'username'),
#         'PASSWORD': CONFIG.get('DB_PASSWORD' ,'password'),
#         'HOST':     CONFIG.get('DB_HOST' ,'127.0.0.1'),
#         'PORT':     CONFIG.get('DB_PORT' ,'5432')
#     }
# }
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE':   database_setting('DB_ENGINE', 'DB_ENGINE' ,'django.db.backends.postgresql_psycopg2'),
            'NAME':     database_setting('POSTGRES_NAME', 'DB_NAME', 'postgres'),
            'USER':     database_setting('POSTGRES_USER', 'DB_USERNAME', 'username'),
            'PASSWORD': database_setting('POSTGRES_PASSWORD' ,'DB_PASSWORD' ,'password'),
            'HOST':     database_setting('POSTGRES_HOST', 'DB_HOST' ,'password'),
            'PORT':     database_setting('DB_PORT', 'DB_PORT' ,'5432')
        }
    }
else:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "PAGE_SIZE": 100,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    # 'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.IsAdminUser', ),
}

# Celery
CELERY_BROKER_URL = database_setting('CELERY_BROKER_URL','CELERY_BROKER_URL','redis://localhost:6379')
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_RESULT_BACKEND = database_setting('CELERY_RESULT_BACKEND','CELERY_RESULT_BACKEND','django-db')
# CELERY_ACCEPT_CONTENT = database_setting('CELERY_ACCEPT_CONTENT','CELERY_ACCEPT_CONTENT',['application/json'])
# CELERY_TASK_SERIALIZER = database_setting('CELERY_TASK_SERIALIZER','CELERY_TASK_SERIALIZER','json')
# CELERY_RESULT_SERIALIZER = database_setting('CELERY_TASK_SCELERY_RESULT_SERIALIZER','CELERY_RESULT_SERIALIZER','json')
# CELERY_TIMEZONE = database_setting('CELERY_TIMEZONE','CELERY_TIMEZONE','Asia/Taipei')
# CELERY_TASK_TRACK_STARTED = True

# CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Taipei'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = database_setting('EMAIL_HOST','EMAIL_HOST','smtp.gmail.com')
EMAIL_PORT = database_setting('EMAIL_PORT','EMAIL_PORT','587')
EMAIL_USE_TLS = database_setting('EMAIL_USE_TLS','EMAIL_USE_TLS',True)
EMAIL_HOST_USER = database_setting('EMAIL_HOST_USER','EMAIL_HOST_USER','')
EMAIL_HOST_PASSWORD = database_setting('EMAIL_HOST_PASSWORD','EMAIL_HOST_PASSWORD','')