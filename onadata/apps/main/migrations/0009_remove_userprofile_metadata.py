# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160831_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='metadata',
        ),
    ]
