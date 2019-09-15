# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_pdffile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PDFFile',
        ),
    ]
