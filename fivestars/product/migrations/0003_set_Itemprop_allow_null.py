# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_create-prop-and-product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemprop',
            options={'verbose_name': '属性名', 'verbose_name_plural': '属性名'},
        ),
        migrations.AlterField(
            model_name='itemprop',
            name='parent_pid',
            field=models.ForeignKey(blank=True, null=True, to='product.ItemProp'),
        ),
        migrations.AlterField(
            model_name='itemprop',
            name='productItem',
            field=models.ForeignKey(blank=True, verbose_name='所属商品', null=True, to='product.models.ItemProps.Product'),
        ),
    ]
