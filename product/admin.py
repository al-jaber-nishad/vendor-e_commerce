from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Brand._meta.fields]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Category._meta.fields]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Color._meta.fields]


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductColor._meta.fields]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Size._meta.fields]


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductSize._meta.fields]