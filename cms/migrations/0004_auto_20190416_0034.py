# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20190415_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation_forarticle',
            name='tite',
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
    ]
