from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in PaymentMethod._meta.fields]


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
	list_display = [field.name for field in OrderStatus._meta.fields]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
	list_display = [field.name for field in OrderItem._meta.fields]


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ShippingAddress._meta.fields]