from django.shortcuts import redirect
from django.urls import path, include, re_path
from django_celery import tasks, views
from django_celery import auto_tasks 

urlpatterns = [
    path('mail/',views.send_email, name='mail')
]