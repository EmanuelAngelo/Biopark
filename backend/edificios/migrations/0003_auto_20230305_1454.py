# Generated by Django 3.0.7 on 2023-03-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificios', '0002_auto_20230305_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartamento',
            old_name='codigo_apartamento',
            new_name='numero_apartamento',
        ),
        migrations.AlterField(
            model_name='apartamento',
            name='descricao',
            field=models.CharField(default='Biopark Apartamentos', max_length=100),
        ),
    ]