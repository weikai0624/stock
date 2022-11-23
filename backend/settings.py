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
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_PATH = os.path.join(BASE_DIR,'config.json')
if os.path.isfile(CONFIG_PATH):
    with open ( os.path.join(BASE_DIR,'config.json'),mode='r',encoding='utf-8' ) as conf:
        CONFIG = json.load(conf)
else:
    CONFIG = {}

def environments_setting(environ_key, default_value):
    return os.environ.get(environ_key, CONFIG.get(environ_key ,default_value))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environments_setting('SECRET_KEY','')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = environments_setting('DEBUG','').lower() in [ True,'true', 't', '1']

# ALLOWED_HOSTS split by ','
ALLOWED_HOSTS = environments_setting('ALLOWED_HOSTS','*').split(',')

CSRF_TRUSTED_ORIGINS = environments_setting('CSRF_TRUSTED_ORIGINS','').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'v1',
    'demo_views',
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

if not os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': {
            'ENGINE':   environments_setting('DB_ENGINE', 'django.db.backends.postgresql_psycopg2'),
            'NAME':     environments_setting('DB_NAME', 'postgres'),
            'USER':     environments_setting('DB_USERNAME', 'username'),
            'PASSWORD': environments_setting('DB_PASSWORD', 'password'),
            'HOST':     environments_setting('DB_HOST', '127.0.0.1'),
            'PORT':     environments_setting('DB_PORT', '5432')
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
    }


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
CELERY_BROKER_URL = environments_setting('CELERY_BROKER_URL','redis://localhost:6379')
CELERY_RESULT_BACKEND = environments_setting('CELERY_RESULT_BACKEND','django-db')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Taipei'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = environments_setting('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = environments_setting('EMAIL_PORT', '587')
EMAIL_USE_TLS = environments_setting('EMAIL_USE_TLS', True)
EMAIL_HOST_USER = environments_setting('EMAIL_HOST_USER', 'username@domain.com')
EMAIL_HOST_PASSWORD = environments_setting('EMAIL_HOST_PASSWORD','password')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')