from django.db import models


class Locatario(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11, unique=True)
    # data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Apartamento(models.Model):
    BLOCO = (
        ('A', 'Aurora'),
        ('B', 'Brasil'),
        ('C', 'Coutry'),
    )
    numero_apartamento = models.CharField(max_length=10)
    descricao = models.CharField(
        max_length=100, default='Biopark Apartamentos')
    bloco = models.CharField(
        max_length=1, choices=BLOCO, blank=False, null=False, default='A')

    def __str__(self):
        return self.numero_apartamento


class Locado(models.Model):
    MODELO = (
        ('Q', 'Quarto'),
        ('A', 'Apartamento'),
    )
    locatario = models.ForeignKey(
        Locatario, verbose_name="Locatario", on_delete=models.CASCADE)
    apartamento = models.ForeignKey(
        Apartamento, verbose_name="Apartamento", on_delete=models.CASCADE)
    modelo = models.CharField(
        max_length=1, choices=MODELO, blank=False, null=False, default='A')
