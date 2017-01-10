# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='类目id', serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='类目名称')),
                ('is_p', models.BooleanField(verbose_name='是否是父级目录', default=False)),
                ('p_id', models.ForeignKey(null=True, to='product.Category', blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'verbose_name': 'category',
            },
        ),
    ]
