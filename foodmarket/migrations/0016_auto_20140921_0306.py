# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmarket', '0015_auto_20140919_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='venmo_authorization_code',
            new_name='venmo_access_token',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='venmo_id',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='venmo_refresh_token',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
