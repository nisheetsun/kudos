from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'', views.BlogViewSet, basename='blog')
router.register(r'content', views.ContentViewSet, basename='content')

urlpatterns = [
    path('', include(router.urls)),
]
