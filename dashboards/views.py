from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def index(request):
     return render(request, 'dashboard/index.html')

@login_required(login_url = 'login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url = 'login')
def products(request):
    return render(request, 'dashboard/products.html')


@login_required(login_url = 'login')
def orders(request):
    return render(request, 'dashboard/orders.html')

