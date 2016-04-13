# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20160413_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='tipo',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
