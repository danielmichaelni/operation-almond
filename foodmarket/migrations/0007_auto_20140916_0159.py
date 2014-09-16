# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0006_dish_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='image',
        ),
        migrations.AddField(
            model_name='dish',
            name='image_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
