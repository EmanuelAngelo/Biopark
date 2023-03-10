from django.db import models
from django.core.exceptions import ValidationError


class Edificio(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numero_apartamento = models.IntegerField(max_length=10)

    def __str__(self):
        return self.nome


class Apartamento(models.Model):
    BLOCO = (
        ('A', 'Aurora'),
        ('B', 'Brasil'),
        ('C', 'Coutry'),
    )
    numero_apartamento = models.CharField(max_length=10)
    numero_quartos = models.IntegerField(max_length=4, default=4)
    max_locatarios = models.IntegerField(default=1)
    descricao = models.CharField(
        max_length=100, default='Biopark Apartamentos')
    bloco = models.CharField(
        max_length=1, choices=BLOCO, blank=False, null=False, default='A')
    edificio = models.ForeignKey(
        Edificio, on_delete=models.CASCADE, related_name='apartamentos')

    def __str__(self):
        return self.numero_apartamento

    def status(self):
        if self.locado_set.count() == 0:
            return "Vazio"
        # elif self.locado_set.count() < self.max_locatarios:
        #     return "Parcialmente ocupado"
        else:
            return "Ocupado"


class Locatario(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11, unique=True)
    # data_nascimento = models.DateField()
    # apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Locado(models.Model):
    MODELO = (
        # ('Q', 'Quarto'),
        ('A', 'Apartamento'),
    )
    locatario = models.ForeignKey(
        Locatario, verbose_name="Locatario", on_delete=models.CASCADE)
    apartamento = models.ForeignKey(
        Apartamento, verbose_name="Apartamento", on_delete=models.CASCADE)
    modelo = models.CharField(
        max_length=1, choices=MODELO, blank=False, null=False, default='A')
    data_inicio = models.DateField(auto_now_add=True)
    data_termino = models.DateField(null=True, blank=True)
    valor_mensal = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    def clean(self):
        if not self.locatario:
            raise ValidationError('E necessário selecionar um locatário.')
        if not self.apartamento:
            raise ValidationError('E necessário selecionar um apartamento.')
        if self.modelo == 'A' and self.apartamento.locado_set.filter(data_termino__isnull=True).exclude(id=self.id).exists():
            raise ValidationError('Este apartamento já está alugado por')
    modelo = models.CharField(
        max_length=1, choices=MODELO, blank=False, null=False, default='A')
