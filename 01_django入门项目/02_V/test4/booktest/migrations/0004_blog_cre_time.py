# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_remove_blog_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cre_time',
            field=models.DateField(default=0, auto_now_add=True),
            preserve_default=False,
        ),
    ]
