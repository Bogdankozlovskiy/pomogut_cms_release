# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPagePomogut', '0005_auto_20190618_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phone', models.CharField(verbose_name='контактный телефон', max_length=17, blank=True, null=True)),
                ('email', models.EmailField(verbose_name='Адрес электронной почты', max_length=254, blank=True, null=True)),
                ('flag', models.BooleanField(verbose_name='отображать эту информацию')),
            ],
            options={
                'verbose_name': 'Контактная информация на сайте',
                'verbose_name_plural': 'Контактная информация на сайте',
            },
        ),
    ]
