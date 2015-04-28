# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codecultform', '0002_auto_20150415_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='summerschoolsignup',
            name='age',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
