from django.conf.urls import url
from django.shortcuts import render
from .import views
# create your views here


urlpatterns = [

    url(r'^$', views.index,name='index'),
]