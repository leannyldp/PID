# Generated by Django 5.0.2 on 2024-02-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RR_HH', '0002_rename_direcciion_trabajador_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivelescolaridad',
            name='descripcion',
            field=models.CharField(choices=[('9no_grado', '9no Grado'), ('tecnico_medio', 'Técnico Medio'), ('12mo_grado', '12mo Grado'), ('universitario', 'Universitario')], max_length=250),
        ),
    ]