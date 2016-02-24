# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160220_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'e-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='artista',
            name='fotos',
            field=models.ManyToManyField(to='main.Imagen', blank=True),
        ),
        migrations.AlterField(
            model_name='artista',
            name='web',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_evento',
            field=models.DateField(verbose_name=b'Fecha'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='precio',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
