# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import feincms.module.medialibrary.fields
import django_ymap.fields
from django.conf import settings
import mptt.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medialibrary', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('name_button', models.CharField(verbose_name='Название кнопки', max_length=100)),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Блок главной страницы',
                'verbose_name_plural': 'Блоки главной страницы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='category name', max_length=50)),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
                ('parent', mptt.fields.TreeForeignKey(verbose_name='parent class', blank=True, null=True, related_name='children', to='cms.Category')),
            ],
            options={
                'verbose_name': 'Раздел-категория-тег',
                'verbose_name_plural': 'Раздел-категория-тег',
                'db_table': 'category',
                'ordering': ('tree_id', 'level'),
            },
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phone', models.CharField(verbose_name='контактный телефон', max_length=20, blank=True, null=True)),
                ('email', models.EmailField(verbose_name='Адрес электронной почты', max_length=254, blank=True, null=True)),
                ('flag', models.BooleanField(verbose_name='отображать эту информацию')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Контактная информация на сайте',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название точки', max_length=200)),
                ('description', models.TextField(verbose_name='описание точки')),
                ('address', django_ymap.fields.YmapCoord(max_length=200)),
            ],
            options={
                'verbose_name': 'Точка',
                'verbose_name_plural': 'Точки',
            },
        ),
        migrations.CreateModel(
            name='Relation_forarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tite', models.CharField(max_length=150)),
                ('pages', models.ManyToManyField(help_text='<b>можно выбрать до 4-х статей.</b><br>', to='page.Page')),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='categories',
            field=models.ManyToManyField(verbose_name='Раздел-категория-тег', to='cms.Category'),
        ),
        migrations.AddField(
            model_name='block',
            name='pages',
            field=models.ManyToManyField(verbose_name='Статьи', to='page.Page'),
        ),
        migrations.AddField(
            model_name='block',
            name='picture',
            field=feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile'),
        ),
    ]
