# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.TextField(max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('web', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('hs_inicio', models.TimeField()),
                ('precio', models.FloatField(null=True)),
                ('fecha_evento', models.DateField()),
                ('fecha_alta', models.DateField(auto_now=True)),
                ('espectaculo', models.ManyToManyField(to='main.Artista')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('momento', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.FileField(upload_to=b'img/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('precio', models.FloatField()),
                ('promocion', models.BooleanField()),
                ('hs_dia', models.ForeignKey(to='main.Horario')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='artista',
            name='fotos',
            field=models.ManyToManyField(to='main.Imagen'),
        ),
        migrations.AddField(
            model_name='artista',
            name='tipo',
            field=models.ForeignKey(to='main.Tipo'),
        ),
    ]
