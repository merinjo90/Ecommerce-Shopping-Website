from django.urls import path,re_path, include, reverse_lazy
# from app import views
from .views import *

from django.contrib.auth import views as auth_views
from .forms import *


urlpatterns = [
    #path('', views.home),
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
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name='login'),
    # path('login/', login, name='login'),
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', checkout, name='checkout'),
]
