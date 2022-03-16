from django.urls import path, re_path, include, reverse_lazy
# from app import views
from .views import *

from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns = [
    # path('', views.home),
    path('', ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart',show_cart,name='showcart'),
    path('buy/', buy_now, name='buy-now'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('mobile/', mobile, name='mobile'),
    path('mobile/<slug:data>', mobile, name='mobiledata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name='login'),
    # path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
                                                                  form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',
                                                                                                form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),

    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', checkout, name='checkout'),
]
