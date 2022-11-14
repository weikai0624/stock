from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pie/$', views.PieView.as_view(), name='pie'),
    url("kline", views.KlineView.as_view(), name='kline')
]

# Create your views here.
