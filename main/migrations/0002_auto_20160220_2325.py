# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagen',
            options={'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Menues'},
        ),
        migrations.AlterField(
            model_name='tipo',
            name='tipo',
            field=models.TextField(max_length=20),
        ),
    ]
