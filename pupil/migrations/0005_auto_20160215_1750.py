# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0004_auto_20160214_1454'),
    ]

    operations = [
    			migrations.DeleteModel(name="User_info"),
    			migrations.DeleteModel(name="User_data"),
    			
    ]
