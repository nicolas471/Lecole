# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160316_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='momento',
            field=models.CharField(max_length=15),
        ),
    ]
