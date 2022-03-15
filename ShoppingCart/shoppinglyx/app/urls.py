from django.urls import path
from .views import *

urlpatterns = [
    # path('', home,name='home'),

    path('', ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', add_to_cart, name='add-to-cart'),
    path('buy/', buy_now, name='buy-now'),
    path('profile/', profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('changepassword/', change_password, name='changepassword'),
    path('mobile/', mobile, name='mobile'),
    path('mobile/<slug:data>', mobile, name='mobiledata'),
    path('login/', login, name='login'),
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', checkout, name='checkout'),
]
