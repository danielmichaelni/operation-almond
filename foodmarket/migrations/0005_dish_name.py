# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0004_auto_20140915_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='name',
            field=models.CharField(default='cookie', max_length=200),
            preserve_default=False,
        ),
    ]
