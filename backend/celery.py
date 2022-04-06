import os
from celery import Celery
from django.conf import settings

# environment variable DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')

app = Celery('backend')

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)