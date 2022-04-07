from django.shortcuts import redirect
from django.urls import path, include, re_path
from django_celery import tasks, views

urlpatterns = [
    path('test/',views.test_celery, name='test'),
    path('mail/',views.test_send_email, name='mail')
]