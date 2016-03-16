# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160316_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='descripcion',
            field=models.TextField(default=b'no posee', max_length=250, null=True, blank=True),
        ),
    ]
