# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0011_auto_20140916_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(related_name=b'vendor', to=settings.AUTH_USER_MODEL),
        ),
    ]
