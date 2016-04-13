# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20160404_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, null=True),
        ),
    ]
