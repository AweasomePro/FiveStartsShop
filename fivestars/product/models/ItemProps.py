import re
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from .category import Category


class ItemProp(models.Model):
    """
    属性名表
    """
    id = models.AutoField(verbose_name='属性id', primary_key=True)
    name = models.CharField(verbose_name='属性名称', max_length=255)
    is_required = models.BooleanField(verbose_name='是否必须', default=False)
    multiChoice = models.BooleanField(verbose_name='是否多选', default=False)
    is_sku = models.BooleanField(verbose_name='是否SKU属性', default=False, help_text=_('在sku属性下，必选属性,sku属性影响库存'))

    parent_pid = models.ForeignKey('self', blank=True, null=True)
    productItem = models.ForeignKey('product.models.ItemProps.Product', verbose_name='所属商品', blank=True, null=True)

    class Meta:
        verbose_name = _('属性名')
        verbose_name_plural = _('属性名')

    def __str__(self):
        return self.name


class ItemPropValue(models.Model):
    """
    属性值表
    """
    id = models.AutoField(verbose_name='属性值id', primary_key=True)
    name = models.CharField(verbose_name='属性值名', blank=False, null=False, max_length=255)
    item_prop = models.ManyToManyField(ItemProp, verbose_name='所属属性')

    class Meta:
        verbose_name = _('属性值')
        verbose_name_plural = _('属性值')

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    某一个产品
    """
    category = models.ForeignKey(Category, verbose_name=_('类别'))
    name = models.CharField(_('商品名'), help_text=_('产品名'), max_length=255)
    sell_name = models.CharField(_('展示名称'), max_length=255, )

    class Meta:
        verbose_name = _('产品')
        verbose_name_plural = _('产品')

    def __str__(self):
        return self.name


class ProductSkuItem(models.Model):
    """
    保存 某个产品的SKU属性
    """
    product = models.ForeignKey(Product, verbose_name=_('所属商品'))
    create_at = models.TimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = _('货品')
        verbose_name_plural = _('货品')

    def __str__(self):
        return self.product.name
        # 出入库表 外键某个sku宝贝
