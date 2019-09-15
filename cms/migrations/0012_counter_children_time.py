# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20190503_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter_children',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
