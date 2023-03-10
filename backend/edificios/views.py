from rest_framework import viewsets
from edificios.models import Locatario, Apartamento, Locado, Edificio
from edificios.serializer import LocatorioSerializer, ApartamentoSerializer, LocadoSerializer, EdificioSerializer


class LocatariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos locatarios"""
    queryset = Locatario.objects.all()
    serializer_class = LocatorioSerializer


class ApartamentoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os apartamentos"""
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer


class LocadoViewSet(viewsets.ModelViewSet):
    """Exbindo apartamentos Locados e por quem"""
    queryset = Locado.objects.all()
    serializer_class = LocadoSerializer


class EdificioViewSet(viewsets.ModelViewSet):
    """Exbindo Edificios"""
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
