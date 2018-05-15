from django.shortcuts import render, redirect
from .models import Product, Order, Customer, Supplier
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
	product = Product.objects.all()
	num_visits=request.session.get('num_visits',0)
	request.session['num_visits'] = num_visits +1
	return render(request, 'home.html', {'product':product,'num_visits':num_visits})
	
def buy(request,pk):
	buy = Product.objects.get(pk=pk)

	if request.method=='POST':
		c_name=request.POST['c_name']
		email=request.POST['email']
		address=request.POST['address']
		qty=request.POST['qty'] 
		total = int(qty)*int(buy.price)
		phone=request.POST['phone']

		customer = Customer.objects.create(
			c_name = c_name,
			email = email,
			address=address,
			phone=phone
			)
		order = Order.objects.create(			
			item=buy,
			qty=qty,
			total=total,
			customer=customer,
			)
		return redirect('home')
		
	return render(request,'buy.html',{'buy':buy})

@user_passes_test(lambda u: u.is_superuser)
def orders(request):
	orders=Order.objects.filter(checked=True).order_by('-order_date')
	return render(request,'orders.html',{'orders':orders})

@user_passes_test(lambda u: u.is_superuser)
def order_detail(request,pk):
	order=Order.objects.get(pk=pk)
	order.checked=False
	order.save(update_fields=['checked'])	
	return render(request,'order_detail.html',{'order':order})

@user_passes_test(lambda u: u.is_superuser)
def checked_orders(request):
	orders=Order.objects.filter(checked=False).order_by('-order_date')
	return render(request,'checked_orders.html',{'orders':orders})

@user_passes_test(lambda u: u.is_superuser)
def checked_order_detail(request,pk):
	order=Order.objects.get(pk=pk)
	return render(request,'checked_order_detail.html',{'order':order})

@user_passes_test(lambda u: u.is_superuser)
def add_items(request):
	if request.method=='POST' and request.FILES['image']:
		p_name=request.POST['p_name']
		description=request.POST['description']
		price=request.POST['price']
		quantity=request.POST['quantity']
		image=request.FILES['image']
		

		Product.objects.create(
			p_name=p_name,
			description=description,
			price=price,
			quantity=quantity,
			image=image,
			)
		return redirect('add_items')
	return render(request,'add_items.html')



