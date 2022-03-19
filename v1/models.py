from django.db import models
import uuid
from django.contrib.auth.models import User, Group
from django.db.models.deletion import DO_NOTHING
from django.db.models.expressions import F
from django.db.models.fields import TextField
# Create your models here.

class UserProfile(models.Model):
    '''
    因為Django 有預設User 因此僅針對沒有的做處理
    '''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.JSONField(null=True)

class GroupProfile(models.Model):
    '''
    因為Django 有預設Group 因此僅針對沒有的做處理
    '''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    profile = models.JSONField(null=True)

class Log(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    ip = models.CharField(editable=True,max_length=100)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    message = models.TextField(editable=True)
    create_time = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True)

class ClassifyType(models.Model):
    name = models.CharField(max_length=1000,unique=True)

class CompanyProfile(models.Model):
    '''
    index =?
    symbol 代號
    major_type = 主要相關類型 本身類型  (唯一) 
    minor_type = 次要相關類型 (以數字字串為主 模糊搜尋用
    '''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=1000,unique=True)
    index = models.FloatField(null=True)
    symbol = models.CharField(max_length=1000,null=True)
    description = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    major_type = models.ForeignKey(ClassifyType,on_delete=DO_NOTHING,null=True)
    minor_type = models.CharField(max_length=1000,null=True)
    last_time = models.DateTimeField(auto_now=True)

class ObjectData(models.Model):
    '''
    method 為 buy sell
    status 為 call put
    type_code 為 deal agaency
    status : 內盤外盤 in out
    '''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    company = models.ForeignKey( CompanyProfile , on_delete=models.DO_NOTHING,related_name="company")
    degree = models.FloatField(null=True)
    method = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    type_code = models.CharField(max_length=10,null=True)
    price = models.FloatField()
    mount = models.IntegerField(null=True)
    percent = models.FloatField(null=True)
    data_time = models.DateTimeField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    contract_date = models.CharField(max_length=100,null=True)
    other = models.JSONField(null=True)
