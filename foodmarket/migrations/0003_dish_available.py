# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0002_auto_20140912_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='available',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
