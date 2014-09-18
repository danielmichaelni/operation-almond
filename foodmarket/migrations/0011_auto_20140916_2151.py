# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0010_auto_20140916_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(verbose_name=b'Price ($)', max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='noworderdish',
            name='num_for_sale',
            field=models.IntegerField(verbose_name=b'Number for sale'),
        ),
    ]
