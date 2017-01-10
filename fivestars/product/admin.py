from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
# Register your models here.

# Register your models here.
# Register your models here.
from .models import *

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(ItemProp)
class ItemPropAdmin(ModelAdmin):
    pass

@admin.register(ItemPropValue)
class ItemPropValueAdmin(ModelAdmin):
    pass

@admin.register(Product)
class ProductItemAdmin(ModelAdmin):
    pass