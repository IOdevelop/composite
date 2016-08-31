# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160830_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='group',
            field=models.CharField(blank=True, max_length=15, choices=[(b'Enumerator', 'Enumerator'), (b'Admin', 'Admin')]),
        ),
    ]
