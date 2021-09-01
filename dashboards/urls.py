from django.urls import path, include
from . import views


urlpatterns= [
    path('dashboard/',views.index, name ='index'),
    path('staff/', views.staff, name = 'dash-staff'),
    path('products/', views.products, name = 'dash-products'),
    path('orders/', views.orders, name = 'dash-orders'),
    path('product_delete/<int:pk>/', views.delete_product, name = 'prod-delete'),
    path('product_update/<int:pk>/', views.update_product, name = 'prod-update'),



]