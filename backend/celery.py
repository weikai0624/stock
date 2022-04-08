from __future__ import absolute_import, unicode_literals
import os
from re import T
from celery import Celery
from django.conf import settings

# environment variable DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')

app = Celery('backend',result_extended=True)

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')