# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0009_auto_20140916_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='rating',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='rating',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=1),
        ),
    ]
