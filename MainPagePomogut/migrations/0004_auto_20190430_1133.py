# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPagePomogut', '0003_auto_20190430_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_contact_us',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
