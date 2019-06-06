# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20190514_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(max_length=20, db_column='title'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
