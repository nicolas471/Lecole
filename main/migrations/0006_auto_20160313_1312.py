# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_imagen_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='fotos',
        ),
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='imagen',
            field=models.ManyToManyField(to='main.Imagen', blank=True),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='img',
            field=models.FileField(upload_to=b'img/%Y/%m/%d', verbose_name=b'Ruta'),
        ),
    ]
