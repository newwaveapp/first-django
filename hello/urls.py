from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('index/', views.index, name ='index'),
    path('stream/', views.stream, name ='stream'),
    path('stream2/', views.stream2, name ='stream2'),
]
