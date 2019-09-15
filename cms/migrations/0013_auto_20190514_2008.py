# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_counter_children_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation',
            name='phone',
            field=models.CharField(verbose_name='контактный телефон', max_length=17, blank=True, null=True),
        ),
    ]
