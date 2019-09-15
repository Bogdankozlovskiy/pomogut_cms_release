# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinformation',
            name='user',
        ),
    ]
