from django.db import models
from django.conf import settings
from authentication.models import Branch, City, Country, Customer
from product.models import Color, Product, Size


# Create your models here.

class PaymentMethod(models.Model):
	name = models.CharField(max_length=255)

	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return str(self.name)
	

class OrderStatus(models.Model):
	name = models.CharField(max_length=255)

	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ('-id', )

	def __str__(self):
		return str(self.name)


class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="orders", null=True, blank=True)
	branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
	order_status = models.ForeignKey(OrderStatus, on_delete= models.SET_NULL, related_name="has_orders", null=True, blank=True) # default=get_default_field(OrderStatus, 'pending'),
	payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)

	order_no = models.CharField(max_length=255, null=True, blank=True)
	tax_price = models.DecimalField(default=0, max_digits=20, decimal_places=2, null=True, blank=True)
	shipping_price = models.DecimalField(default=0, max_digits=20, decimal_places=2, null=True, blank=True)
	pay_amount = models.DecimalField(default=0, max_digits=20, decimal_places=2, null=True, blank=True)
	return_amount = models.DecimalField(default=0, max_digits=20, decimal_places=2, null=True, blank=True)

	net_amount = models.DecimalField(default=0, max_digits=50, decimal_places=2, null=True, blank=True)
	grand_total = models.DecimalField(default=0, max_digits=50, decimal_places=2, null=True, blank=True)
	order_date = models.DateTimeField(null=True, blank=True)
	comment = models.TextField(null=True, blank=True)

	is_delivered = models.BooleanField(default=False, null=True, blank=True)
	is_paid = models.BooleanField(default=False, null=True, blank=True)

	paid_at = models.DateTimeField(null=True, blank=True)
	delivered_at = models.DateTimeField(null=True, blank=True)
	
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

	delivered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="delivered", null=True, blank=True)
	cancelled_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="cancelled", null=True, blank=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ['-id']

	def __str__(self, ):
		return str(self.id)	


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order_items', null=True)
	
	color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
	size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)

	quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
	price = models.DecimalField(default=0, max_digits=20, decimal_places=2, null=True, blank=True)
	subtotal = models.DecimalField(default=0, max_digits=20, decimal_places=2, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		verbose_name_plural = 'OrderItems'

	def __str__(self):
		return str(self.id)


class ShippingAddress(models.Model):
	name = models.CharField(max_length=30, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, null=True, blank=True)
	order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)

	shipping_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	company = models.CharField(max_length=50, null=True, blank=True)
	street_address = models.CharField(max_length=255, null=True, blank=True)
	city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
	zip_code = models.CharField(max_length=50, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ('-id', )
	
	def __str__(self):
		return str(self.street_address)