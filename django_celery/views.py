import re
from django.http import JsonResponse
from django_celery import tasks 
from drf_yasg.utils import swagger_auto_schema
from celery.result import AsyncResult
from rest_framework import  generics
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg import openapi

# Create your views here.


def send_email(request,*args,**kwargs):
    recipient_email = request.GET.get('recipient_email',None)
    recipient_name = request.GET.get('recipient_name',None)
    if recipient_email != None and recipient_name != None:
        res=tasks.send_email.delay(recipient_email,recipient_name)
        result = AsyncResult(res.task_id)
        print('send_email',result)
        return JsonResponse({'status':result.status,'task_id':result.task_id})
    else:
        return JsonResponse({'status':None,'task_id':None})

class SendEmailViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        operation_summary='寄送Email',
        operation_description='使用非同步進行寄送Email',
        manual_parameters=[
            openapi.Parameter('recipient_email', openapi.IN_QUERY, description="收件者email", type=openapi.TYPE_STRING),
            openapi.Parameter('recipient_name', openapi.IN_QUERY, description="收件者名稱", type=openapi.TYPE_STRING)
        ]
    )

    def get(self, request, format=None):
        recipient_email = request.GET.get('recipient_email',None)
        recipient_name = request.GET.get('recipient_name',None)
        if recipient_email != None and recipient_name != None:
            print(recipient_email,recipient_name)
            res=tasks.send_email.delay(recipient_email,recipient_name)
            result = AsyncResult(res.task_id)
            print('send_email',result)
            return Response({'status':result.status,'task_id':result.task_id})
        else:
            return Response({'status':None,'task_id':None})