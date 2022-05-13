from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from Eshop.settings import BASE_DIR
import os

'''
def contact_us(request):
    if request.method == 'GET':
        print(os.path.join(BASE_DIR, 'template'))
        template = loader.get_template('contact_us.html')
        send_mail(
    'Subject here',
    'Here is the message.',
    'akkyaryan6@gmail.com',
    ['akkyaryan6@gmail.com'],
    fail_silently=False,
        )  # getting our template
        return HttpResponse(template.render())
    if request.method == 'POST':
        return HttpResponseRedirect("/")
'''
@csrf_exempt
def contact_us(request):
    if request.method == 'POST':
        name=request.POST.get('full-name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        data={
           'name':name,
           'email':email,
           'subject':subject,
           'message':message,
        }

        message='''
        New message:{}

        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'',['akkyaryan6@gmail.com'])

    return render(request,'contact_us.html',{})

    '''if request.method == 'GET':
        print(os.path.join(BASE_DIR, 'template'))
        template = loader.get_template('contact_us.html')
        return HttpResponse(template.render())'''
