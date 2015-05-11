# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codecultform', '0003_summerschoolsignup_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='summerschoolsignup',
            name='parent',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
