# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432\u044b \u043f\u043e ID \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0435',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b \u043f\u043e ID \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0435',
            },
        ),
    ]
