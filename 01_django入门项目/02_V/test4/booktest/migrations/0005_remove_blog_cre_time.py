# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_blog_cre_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='cre_time',
        ),
    ]
