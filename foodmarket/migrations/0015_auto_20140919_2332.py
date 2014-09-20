# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0014_auto_20140919_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='availability_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dish',
            name='deadline_to_order',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dish',
            name='num_available',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dish',
            name='num_for_sale',
            field=models.IntegerField(null=True, verbose_name=b'Number for sale'),
            preserve_default=True,
        ),
    ]
