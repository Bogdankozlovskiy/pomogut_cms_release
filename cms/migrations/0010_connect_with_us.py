# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20190429_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect_with_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('target_message', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
    ]
