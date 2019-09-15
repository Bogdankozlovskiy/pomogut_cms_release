# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPagePomogut', '0004_auto_20190430_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='help_for_addicts_links',
            options={'verbose_name': 'Сcылки для "Помощь наркозависимым"', 'verbose_name_plural': 'Сcылки для "Помощь наркозависимым"'},
        ),
        migrations.AlterField(
            model_name='help_for_addicts_links',
            name='title',
            field=models.CharField(verbose_name='название ссылки', max_length=25),
        ),
        migrations.AlterField(
            model_name='network_security_links',
            name='title',
            field=models.CharField(verbose_name='название ссылки', max_length=25),
        ),
    ]
