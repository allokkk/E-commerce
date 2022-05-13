from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from Eshop.settings import BASE_DIR
import os




"""
def pay(request):
    print(os.path.join(BASE_DIR, 'template'))
    template = loader.get_template('pay.html')  # getting our template
    return HttpResponse(template.render())
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Eshop.settings import BASE_DIR
import os
from django.views import View
import razorpay
from django.shortcuts import render
from Eshop.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY


# Create your views here.

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def pay(request):
    print(request.session)
    order_amount=40000
    order_currency='IN'
    order_receipt=''
    payment_order=client.order.create(dict(amount=order_amount,currency=order_currency, payment_capture=1))
    payment_order_id=payment_order['id']





    context ={
    'amount':order_amount,'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id
    }
    return render(request,'pay.html',context)
    '''
    print(os.path.join(BASE_DIR, 'template'))
    template = loader.get_template('home.html')  # getting our template
    return HttpResponse(template.render())
    '''
