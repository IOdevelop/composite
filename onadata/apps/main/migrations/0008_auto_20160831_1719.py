# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160830_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='home_page',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='twitter',
        ),
    ]
