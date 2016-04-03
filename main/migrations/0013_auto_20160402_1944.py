# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160325_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Seteos Generales',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.TextField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='seccion',
            field=models.ForeignKey(to='main.Section'),
        ),
    ]
