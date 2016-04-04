# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20160402_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='titulo',
            field=models.CharField(default=b'no posee', max_length=50),
        ),
    ]
