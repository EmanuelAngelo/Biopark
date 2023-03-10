from django.contrib import admin
from django.urls import path, include
from edificios.views import ApartamentoViewSet, LocatariosViewSet, LocadoViewSet, EdificioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('locatarios', LocatariosViewSet, basename='Locatarios')
router.register('apartamentos', ApartamentoViewSet, basename='Apartamentos')
router.register('locados', LocadoViewSet, basename='Locados')
router.register('edificios', EdificioViewSet, basename='Edificios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
