# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0012_auto_20140916_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='vendor',
            field=models.ForeignKey(related_name=b'dish', to='foodmarket.Vendor'),
        ),
    ]
