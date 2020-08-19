from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index')

]