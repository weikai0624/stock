import time
# from __future__ import absolute_import
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

# extention one task
@shared_task
def send_email(recipient_email, recipient_name): 
    subject = 'Test sending email'
    message = 'hello {}'.format(recipient_name)
    mail_sent = send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, # 寄件人的信箱
            [recipient_email] # 收件人的信箱
    )
    print('test: send_email')
    return mail_sent


@shared_task
def args_add1(x,y):
    print("start task no.1 now!")
    time.sleep(10)
    print("task no.1 end!")
    return x+y

# print('test: ',send_email('weikai@fucotech.com.tw','Weikai'))