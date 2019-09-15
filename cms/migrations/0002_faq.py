# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('request', models.CharField(verbose_name='чысто задаваемый вопрос', max_length=150)),
                ('response', models.TextField(verbose_name='Ответ:')),
            ],
        ),
    ]
