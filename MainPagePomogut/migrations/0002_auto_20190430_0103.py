# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPagePomogut', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='To_contact_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.URLField()),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Связаться с нами',
                'verbose_name_plural': 'Связаться с нами',
                'db_table': 'Связаться с нами',
            },
        ),
        migrations.AlterModelOptions(
            name='network_security_links',
            options={'verbose_name': 'Ссылки для "Безопасность в сети"', 'verbose_name_plural': 'Ссылки для "Безопасность в сети"'},
        ),
    ]
