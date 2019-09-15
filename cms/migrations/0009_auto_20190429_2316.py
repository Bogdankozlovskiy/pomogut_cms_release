# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_encyclopedia_of_knowledge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='encyclopedia_of_knowledge',
            options={'verbose_name': 'Энциклопедия знаний', 'verbose_name_plural': 'Энциклопедия знаний'},
        ),
    ]
