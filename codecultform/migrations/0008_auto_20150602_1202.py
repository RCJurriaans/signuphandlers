# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codecultform', '0007_summerschoolsignup_parent_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summerschoolsignup',
            name='age',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
