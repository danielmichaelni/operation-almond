# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0008_review_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image_url',
            field=models.URLField(verbose_name=b'Image URL (optional)', blank=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='rating',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1),
        ),
    ]
