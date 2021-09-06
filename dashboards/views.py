from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required(login_url = 'login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    staff = User.objects.all()
    staff_count = staff.count()
    products_count = products.count()
    orders_count = orders.count()



    if request.method =='POST':
         form = OrderForm(request.POST)
         if form.is_valid():
             instance =form.save(commit = False)
             instance.staff = request.user
             instance.save()
             return redirect('index')


    else:
        form = OrderForm()
    context = {
        'staff':staff,
        'orders': orders,
        'form': form,
        'products': products,
        'staff_count':staff_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url = 'login')
def staff(request):
    staff = User.objects.all() 
    orders = Order.objects.all()
    products = Product.objects.all()
    staff_count = staff.count()
    products_count = products.count()
    orders_count = orders.count()

    context= {
        'staff':staff,
        'staff_count': staff_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/staff.html',context)


@login_required(login_url = 'login')
def staff_details(request,pk):
    staff = User.objects.get(id=pk)
    context= {
        'staff':staff,
    }

    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url = 'login')
def products(request):
    prods = Product.objects.all()
    products_count = prods.count()
    staff = User.objects.all() 
    orders = Order.objects.all()
    staff_count = staff.count()
    orders_count = orders.count()

    

    if request. method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added successfully')
        return redirect ('dash-products')
    else:
        form = ProductForm()

    # prods = Product.objects.raw ('SELECT * FROM dashboards_product') # using Raw sql
    context= {
        'prods':prods,
        'form' : form,
        'products_count': products_count,
        'orders_count': orders_count,
        'staff_count':staff_count


    }
    return render(request, 'dashboard/products.html', context)


@login_required(login_url = 'login')
def orders(request):

    order = Order.objects.all()
    orders_count = order.count()
    prods = Product.objects.all()
    products_count = prods.count()
    staff = User.objects.all() 
    staff_count = staff.count()

    context= {
        'order':order,
        'orders_count':orders_count,
        'staff_count':staff_count,
        'products_count':products_count
    }
    return render(request, 'dashboard/orders.html',context)

@login_required(login_url = 'login')
def delete_product(request,pk):
    item = Product.objects.get(id =pk)
    if request.method == 'POST':
        item.delete()
        return redirect ('dash-products')


    return  render (request, 'dashboard/delete_product.html')


@login_required(login_url = 'login')

def update_product(request,pk):
    item = Product.objects.get(id =pk)

    if  request.method == 'POST':
        form = ProductForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect ('dash-products')
    else:
        form = ProductForm( instance=item)


    context = {
        'form': form,

    }
    return render (request, 'dashboard/product_update.html',context)