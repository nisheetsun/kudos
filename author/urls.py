from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from . import views

router = DefaultRouter()
router.register(r'', views.AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls))
]
