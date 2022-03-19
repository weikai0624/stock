import imp
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v1.api.company import CompanyAPI
from v1.api.classify import ClassifyTypeAPI
from v1.api.stock_data import DataAPI


router = DefaultRouter()
router.register(r'company', ClassifyTypeAPI, basename='company')
router.register(r'classifytype', CompanyAPI, basename='classifytype')
router.register(r'data', DataAPI, basename='data')

urlpatterns = [
]

urlpatterns += router.urls


