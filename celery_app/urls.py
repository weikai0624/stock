from django.shortcuts import redirect
from django.urls import path, include, re_path
from celery_app import tasks, views

urlpatterns = [
    path('test/',views.test_celery, name='test'),
    path('mail/',views.send_email, name='mail')
]