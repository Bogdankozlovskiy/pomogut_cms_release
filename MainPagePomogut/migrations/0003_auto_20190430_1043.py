# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import feincms.module.medialibrary.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MainPagePomogut', '0002_auto_20190430_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help_for_addicts_links',
            name='mediafile',
            field=feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile'),
        ),
        migrations.AlterField(
            model_name='network_security_links',
            name='mediafile',
            field=feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile'),
        ),
    ]
