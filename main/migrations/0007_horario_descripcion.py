# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160313_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='descripcion',
            field=models.TextField(default=b'no posee', max_length=250),
        ),
    ]
