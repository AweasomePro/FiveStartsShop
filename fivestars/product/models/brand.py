import re
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from .category import Category


class Brand(models.Model):
    """
    产品品牌
    """
    id = models.AutoField(verbose_name='品牌', primary_key=True)
    category = models.ForeignKey(Category,verbose_name=_('所属类别'))
    name = models.CharField(verbose_name='品牌名称', max_length=255)

    class Meta:
        verbose_name = _('品牌')
        verbose_name_plural = _('品牌')
