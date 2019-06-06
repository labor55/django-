# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 27, 8, 46, 16, 906000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
