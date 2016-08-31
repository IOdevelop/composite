# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_userprofile_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='group',
            field=models.CharField(blank=True, max_length=3, choices=[(b'ENU', 'Enumerator'), (b'ADM', 'Admin')]),
        ),
    ]
