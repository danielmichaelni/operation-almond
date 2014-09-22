# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.encrypted


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0016_auto_20140921_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='test_field',
            field=django_extensions.db.fields.encrypted.EncryptedCharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
