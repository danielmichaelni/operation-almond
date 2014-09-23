# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0018_auto_20140922_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='require_pre_order',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
