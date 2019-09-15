# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import feincms.module.medialibrary.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help_for_addicts_links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('title', models.CharField(verbose_name='название ссылки', max_length=150)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Сылки для "Помощь наркозависимым"',
                'verbose_name_plural': 'Сылки для "Помощь наркозависимым"',
                'db_table': 'Помощь наркозависимым',
            },
        ),
        migrations.CreateModel(
            name='Network_security_links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('title', models.CharField(verbose_name='название ссылки', max_length=150)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Ссылка для "Безопасность в сети"',
                'verbose_name_plural': 'Ссылка для "Безопасность в сети"',
                'db_table': 'Безопасность в сети',
            },
        ),
    ]
