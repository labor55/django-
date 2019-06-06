# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_blog_created_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_time',
        ),
    ]
