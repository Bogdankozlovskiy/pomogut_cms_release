# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import feincms.module.medialibrary.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20190416_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='picture',
            field=feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile'),
        ),
        migrations.AlterField(
            model_name='block',
            name='slug',
            field=models.SlugField(verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='block',
            name='title',
            field=models.CharField(verbose_name='Название блока', max_length=100),
        ),
        migrations.AlterField(
            model_name='faq',
            name='request',
            field=models.CharField(verbose_name='Часто задаваемый вопрос', max_length=150),
        ),
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.URLField(verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(verbose_name='название', max_length=150),
        ),
    ]
