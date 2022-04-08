import re
from django.http import JsonResponse
from django_celery import tasks 
from celery.result import AsyncResult

# Create your views here.


def send_email(request,*args,**kwargs):
    recipient_email = request.GET.get('recipient_email',None)
    recipient_name = request.GET.get('recipient_name',None)
    if recipient_email != None and recipient_name != None:
        res=tasks.send_email.delay('weikai@fucotech.com.tw','WEIKAI')
        result = AsyncResult(res.task_id)
        print('send_email',result)
        return JsonResponse({'status':result.status,'task_id':result.task_id})
    else:
        return JsonResponse({'status':None,'task_id':None})