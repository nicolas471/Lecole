# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20160316_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='precio',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
