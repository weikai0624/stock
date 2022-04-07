from django.http import JsonResponse
from django_celery import tasks 
from celery.result import AsyncResult

# Create your views here.

def test_celery(request,*args,**kwargs):
    res=tasks.args_add1.delay(123,456) 
    result = AsyncResult(res.task_id)
    print('test: test_celery',result)
    return JsonResponse({'status':result.status,'task_id':result.task_id})

def test_send_email(request,*args,**kwargs):
    res=tasks.send_email.delay('weikai@fucotech.com.tw','WEIKAI')
    result = AsyncResult(res.task_id)
    print('test: send_email',result)
    return JsonResponse({'status':result.status,'task_id':result.task_id})