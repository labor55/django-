# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='comment',
            new_name='bcomment',
        ),
        migrations.RenameField(
            model_name='bookinfo',
            old_name='pub_date',
            new_name='bpub_date',
        ),
        migrations.RenameField(
            model_name='bookinfo',
            old_name='read',
            new_name='bread',
        ),
        migrations.RenameField(
            model_name='bookinfo',
            old_name='title',
            new_name='btitle',
        ),
        migrations.RenameField(
            model_name='bookinfo',
            old_name='isDalete',
            new_name='isDelete',
        ),
        migrations.RenameField(
            model_name='heroinfo',
            old_name='book',
            new_name='hbook',
        ),
        migrations.RenameField(
            model_name='heroinfo',
            old_name='gender',
            new_name='hgender',
        ),
        migrations.RenameField(
            model_name='heroinfo',
            old_name='name',
            new_name='hname',
        ),
        migrations.RenameField(
            model_name='heroinfo',
            old_name='isDalete',
            new_name='isDelete',
        ),
    ]
