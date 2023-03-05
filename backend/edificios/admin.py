from django.contrib import admin
from edificios.models import Locatario, Apartamento, Locado


class Locatarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Locatario, Locatarios)


class Apartamentos(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento', 'descricao', 'bloco')
    list_display_links = ('id', 'numero_apartamento')
    search_fields = ('numero_apartamento',)


admin.site.register(Apartamento, Apartamentos)


class Alocado(admin.ModelAdmin):
    list_display = ('id', 'locatario', 'apartamento', 'modelo')
    list_display_links = ('id',)


admin.site.register(Locado, Alocado)
