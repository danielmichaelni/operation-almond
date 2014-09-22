# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.encrypted


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0017_userprofile_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='test_field',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='venmo_access_token',
            field=django_extensions.db.fields.encrypted.EncryptedCharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='venmo_id',
            field=django_extensions.db.fields.encrypted.EncryptedCharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='venmo_refresh_token',
            field=django_extensions.db.fields.encrypted.EncryptedCharField(max_length=200),
        ),
    ]
