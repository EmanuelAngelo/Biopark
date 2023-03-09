from rest_framework import serializers
from edificios.models import Locatario, Apartamento, Locado


class LocatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locatario
        fields = ['id', 'nome', 'rg', 'cpf']


class ApartamentoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Apartamento
        fields = ['id', 'numero_apartamento',
                  'max_locatarios', 'descricao', 'bloco', 'status']

    def get_status(self, obj):
        return obj.status()


class LocadoSerializer(serializers.ModelSerializer):
    locatario = LocatorioSerializer(many=False)
    apartamento = serializers.PrimaryKeyRelatedField(
        queryset=Apartamento.objects.all())

    class Meta:
        model = Locado
        fields = ['id', 'locatario', 'apartamento']
