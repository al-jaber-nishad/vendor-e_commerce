from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Role._meta.fields]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Country._meta.fields]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = [field.name for field in City._meta.fields]


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Branch._meta.fields]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Customer._meta.fields]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Vendor._meta.fields]

