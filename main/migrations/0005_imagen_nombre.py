# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160223_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default=b'imagen', max_length=30),
        ),
    ]
