# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SummerSchoolSignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('email', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=2, choices=[(b'AM', b'Amsterdam'), (b'UT', b'Utrecht'), (b'AR', b'Arnhem')])),
                ('message', models.TextField()),
            ],
        ),
    ]
