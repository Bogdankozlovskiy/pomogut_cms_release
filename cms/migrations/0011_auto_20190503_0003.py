# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_connect_with_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter_children',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('couner1', models.IntegerField(default=0)),
                ('couner2', models.IntegerField(default=0)),
                ('couner3', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Счетчик',
                'verbose_name_plural': 'Счетчик',
            },
        ),
        migrations.AlterModelOptions(
            name='connect_with_us',
            options={'verbose_name': 'Форма обратной связи', 'verbose_name_plural': 'Форма обратной связи'},
        ),
    ]
