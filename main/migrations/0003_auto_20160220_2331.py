# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160220_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
    ]
