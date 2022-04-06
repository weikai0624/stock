from django.http import JsonResponse
from celery_app import tasks 
from celery.result import AsyncResult

# Create your views here.

def test_celery(request,*args,**kwargs):
    res=tasks.args_add1.delay(123,456) #傳送任務給celery  
    result = AsyncResult(res.task_id)
    print('test: test_celery',result)
    return JsonResponse({'status':result.status,'task_id':result.task_id})

def send_email(request,*args,**kwargs):
    res=tasks.send_email.delay('weikai@fucotech.com.tw','WEIKAI')
    result = AsyncResult(res.task_id)
    print('test: send_email',result)
    return JsonResponse({'status':result.status,'task_id':result.task_id})