# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0007_auto_20140916_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
