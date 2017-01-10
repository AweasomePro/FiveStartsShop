import re
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """
    产品类目
    """
    id = models.AutoField(verbose_name='类目id', primary_key=True)
    name = models.CharField(verbose_name='类目名称', max_length=255)
    is_p = models.BooleanField(verbose_name='是否是父级目录', default=False)
    p_id = models.ForeignKey('self', null=True, blank=True, )

    class Meta:
        verbose_name = _('类目')
        verbose_name_plural = _('类目')

    def __str__(self):
        return self.name
