# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_set_Itemprop_allow_null'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': '品牌', 'verbose_name': '品牌'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '类目', 'verbose_name': '类目'},
        ),
        migrations.AlterModelOptions(
            name='itempropvalue',
            options={'verbose_name_plural': '属性值', 'verbose_name': '属性值'},
        ),
        migrations.AlterModelOptions(
            name='productitem',
            options={'verbose_name_plural': '产品', 'verbose_name': '产品'},
        ),
        migrations.AddField(
            model_name='productitem',
            name='category',
            field=models.ForeignKey(verbose_name='类别', to='product.Category', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='id',
            field=models.AutoField(verbose_name='品牌', primary_key=True, serialize=False),
        ),
    ]
