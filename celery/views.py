from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

send_email.delay(<recipient_email>, '<recipient_name>')