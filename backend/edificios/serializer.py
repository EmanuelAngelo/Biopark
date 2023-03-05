from rest_framework import serializers
from edificios.models import Locatario, Apartamento


class LocatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locatario
        fields = ['id', 'nome', 'rg', 'cpf']


class ApartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartamento
        fields = '__all__'
