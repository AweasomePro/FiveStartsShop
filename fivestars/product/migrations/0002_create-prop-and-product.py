# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_create-category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='品牌id', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='品牌名称', max_length=255)),
                ('category', models.ForeignKey(verbose_name='所属类别', to='product.Category')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='ItemProp',
            fields=[
                ('id', models.AutoField(verbose_name='属性id', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='属性名称', max_length=255)),
                ('is_required', models.BooleanField(verbose_name='是否必须', default=False)),
                ('multiChoice', models.BooleanField(verbose_name='是否多选', default=False)),
                ('is_sku', models.BooleanField(verbose_name='是否SKU属性', help_text='在sku属性下，必选属性,sku属性影响库存', default=False)),
                ('parent_pid', models.ForeignKey(to='product.ItemProp')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='ItemPropValue',
            fields=[
                ('id', models.AutoField(verbose_name='属性值id', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='属性值名', max_length=255)),
                ('item_prop', models.ManyToManyField(verbose_name='所属属性', to='product.ItemProp')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='商品名', max_length=255, help_text='产品名')),
                ('sell_name', models.CharField(verbose_name='展示名称', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductItemSku',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='itemprop',
            name='productItem',
            field=models.ForeignKey(verbose_name='所属商品', to='product.models.ItemProps.Product'),
        ),
    ]
