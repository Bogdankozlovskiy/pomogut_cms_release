# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_remove_contactinformation_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactInformation',
        ),
    ]
