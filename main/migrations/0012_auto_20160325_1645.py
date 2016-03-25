# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20160316_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='img',
            field=models.ImageField(upload_to=b'img/%Y/%m/%d', verbose_name=b'Ruta'),
        ),
    ]
