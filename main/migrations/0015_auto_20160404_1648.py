# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_generalsetting_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='img',
            field=models.ImageField(upload_to=b'imgenEvento', verbose_name=b'Ruta'),
        ),
    ]
