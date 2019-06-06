# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_pictest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('read', models.IntegerField(default=0)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='areainfo',
            name='atitle',
            field=models.CharField(verbose_name='标题', max_length=30),
        ),
    ]
