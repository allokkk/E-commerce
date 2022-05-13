from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
import os
from .views.about_us import about_us
from .views.pay import pay
from .views.contact_us import contact_us


from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware

from django.contrib import admin
from django.urls import path, include


urlpatterns = [



    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('about_us', about_us, name='about_us'),
    path('pay', pay, name='pay'),

    path('contact_us', contact_us, name='contact_us'),




    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]
