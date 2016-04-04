# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20160404_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='imagen',
        ),
        migrations.AddField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(default=b'\\media\\imagenEvento\\default.jpg', upload_to=b'imgenEvento', verbose_name=b'Ruta'),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
