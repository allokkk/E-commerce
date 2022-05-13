from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from Eshop.settings import BASE_DIR
import os





def about_us(request):
    print(os.path.join(BASE_DIR, 'template'))
    template = loader.get_template('about_us.html')  # getting our template
    return HttpResponse(template.render())
