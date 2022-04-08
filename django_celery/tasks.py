import time
# from __future__ import absolute_import
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

# extention one task
@shared_task
def send_email(recipient_email, recipient_name): 
    subject = 'Test sending email'
    message = 'Hi, {}'.format(recipient_name)
    mail_sent = send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, # 寄件人的信箱
            [recipient_email] # 收件人的信箱
    )
    return mail_sent

