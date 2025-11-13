from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'juegos ', JuegoViewSet, basename='juego')
router.register(r'usuarios ', UsuarioViewSet, basename='usuario')
router.register(r'reviews ', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]

