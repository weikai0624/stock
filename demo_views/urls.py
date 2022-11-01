from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pie/$', views.PieView.as_view(), name='demo')
]

# Create your views here.
