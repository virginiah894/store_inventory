from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductForm
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url = 'login')
def index(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url = 'login')
def staff(request):
    staff = User.objects.all() 
    context= {
        'staff':staff,
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

    if request. method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('dash-products')
    else:
        form = ProductForm()

    # prods = Product.objects.raw ('SELECT * FROM dashboards_product') # using Raw sql
    context= {
        'prods':prods,
        'form' : form,
    }
    return render(request, 'dashboard/products.html', context)


@login_required(login_url = 'login')
def orders(request):

    order = Order.objects.all()
    context= {
        'order':order,
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