# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AlterModelOptions(
            name='relation_forarticle',
            options={'verbose_name': 'Группа статей'},
        ),
        migrations.AddField(
            model_name='category',
            name='flag',
            field=models.BooleanField(verbose_name='Стадия разработки', default=False, help_text='Страницы будут не доступны для пользователя'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(verbose_name='Родитель', blank=True, null=True, related_name='children', to='cms.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(verbose_name='Название', max_length=50),
        ),
        migrations.AlterField(
            model_name='relation_forarticle',
            name='pages',
            field=models.ManyToManyField(verbose_name='Статьи', help_text='<b>можно выбрать до 4-х статей.</b><br>', to='page.Page'),
        ),
        migrations.AlterField(
            model_name='relation_forarticle',
            name='tite',
            field=models.CharField(verbose_name='название группы', max_length=150, blank=True, null=True),
        ),
    ]
