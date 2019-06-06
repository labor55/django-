# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='modifified_time',
            new_name='modified_time',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='pws',
            new_name='pwd',
        ),
    ]
