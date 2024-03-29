from django.shortcuts import redirect
from django.urls import path, include, re_path
from django_celery import views

urlpatterns = [
    path('mail/', views.send_email, name='mail'),
    path('sendmail/', views.SendEmailViewSet.as_view(), name='sendmail'),
    path('status/<str:celery_id>', views.CeleryStatus.as_view(), name='celery_status'),
]