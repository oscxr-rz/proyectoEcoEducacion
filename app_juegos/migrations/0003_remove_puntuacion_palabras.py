# Generated by Django 5.1.3 on 2024-11-13 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_juegos', '0002_rename_juego1_puntuacion_palabras_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puntuacion',
            name='palabras',
        ),
    ]
