# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0013_auto_20140916_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noworderdish',
            name='dish_ptr',
        ),
        migrations.DeleteModel(
            name='NowOrderDish',
        ),
        migrations.RemoveField(
            model_name='preorderdish',
            name='dish_ptr',
        ),
        migrations.DeleteModel(
            name='PreOrderDish',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='venmo_authorization_code',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
