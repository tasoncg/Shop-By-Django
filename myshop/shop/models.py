from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Supplier(models.Model):
	s_name = models.CharField(max_length=200)
	last_supply_date = models.DateField(auto_now=True)
	def __str__(self):
		return self.s_name

class Product(models.Model):
	p_name = models.CharField(max_length=30, unique = True)
	description = models.CharField(max_length=100)
	price = models.IntegerField()
	quantity = models.IntegerField( blank=True)
	supplier = models.ForeignKey(Supplier, related_name='supplier', null=True, blank = True, on_delete=models.DO_NOTHING)
	image = models.FileField(blank=True, null=True)
	sale = models.BooleanField(default=False,)

	def __str__(self):
		return self.p_name

class Customer(models.Model):
	c_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	address = models.CharField(max_length=254)
	last_buy_date = models.DateField(auto_now_add=True)
	phone = models.IntegerField(default=0)
	def __str__(self):
		return self.c_name

class Order(models.Model):
	item = models.ForeignKey(Product,related_name='product',on_delete=models.DO_NOTHING)
	qty = models.IntegerField(default=1)
	total = models.IntegerField()
	order_date = models.DateField(auto_now_add=True)
	customer = models.ForeignKey(Customer, related_name='customer',on_delete=models.DO_NOTHING)
	checked=models.BooleanField(default=True)
	def __str__(self):
		return self.customer.c_name

