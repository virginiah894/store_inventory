from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductForm

# Create your views here.
@login_required(login_url = 'login')
def index(request):
     return render(request, 'dashboard/index.html')

@login_required(login_url = 'login')
def staff(request):
    staff = user.objects.all 
    context= {
        'staff':staff,
    }
    return render(request, 'dashboard/staff.html')

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

    order = Order.objects.all 
    context= {
        'order':order,
    }
    return render(request, 'dashboard/orders.html')

def delete_product(request,pk):
    item = Product.objects.get(id =pk)
    if request.method == 'POST':
        item.delete()
        return redirect ('dash-products')


    return  render (request, 'dashboard/delete_product.html')



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