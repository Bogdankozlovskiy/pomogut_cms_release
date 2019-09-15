# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20190423_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encyclopedia_of_knowledge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('request', models.CharField(verbose_name='Часто задаваемый вопрос', max_length=150)),
                ('response', models.TextField(verbose_name='Ответ:')),
            ],
            options={
                'verbose_name': 'Энциклопедия знаний',
            },
        ),
    ]
