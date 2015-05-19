# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codecultform', '0005_auto_20150519_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summerschoolsignup',
            name='city',
            field=models.CharField(max_length=2, choices=[(b'AM', b'Amsterdam (6-10 Juli)'), (b'A2', b'Amsterdam (13-17 Juli)'), (b'UT', b'Utrecht (17-21 Augustus)'), (b'AR', b'Arnhem (24-28 Augustus)')]),
        ),
    ]
