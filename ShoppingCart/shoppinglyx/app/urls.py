
from django.urls import path
# from app import views
# urlpatterns = [
#     path('', views.home),
#     path('product-detail/', views.product_detail, name='product-detail'),
#     path('cart/', views.add_to_cart, name='add-to-cart'),
#     path('buy/', views.buy_now, name='buy-now'),
#     path('profile/', views.profile, name='profile'),
#     path('address/', views.address, name='address'),
#     path('orders/', views.orders, name='orders'),
#     path('changepassword/', views.change_password, name='changepassword'),
#     path('mobile/', views.mobile, name='mobile'),
#     path('login/', views.login, name='login'),
#     path('registration/', views.customerregistration, name='customerregistration'),
#     path('checkout/', views.checkout, name='checkout'),
# ]

from .views import *


urlpatterns = [
    path('', home),
    path('product-detail/', product_detail, name='product-detail'),
    path('cart/', add_to_cart, name='add-to-cart'),
    path('buy/', buy_now, name='buy-now'),
    path('profile/',profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('changepassword/', change_password, name='changepassword'),
    path('mobile/', mobile, name='mobile'),
    path('login/', login, name='login'),
    path('registration/', customerregistration, name='customerregistration'),
    path('checkout/', checkout, name='checkout'),
]