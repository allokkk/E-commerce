from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
import razorpay
from store.models.product import Products
from store.models.orders import Order
from Eshop.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

class CheckOut(View):
    def post(self, request):
        client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        print(cart)
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        total_price = 0
        for product in products:
            print('quantity',cart.get(str(product.id)))
            print('price',product.price)
            # print(cart.get(str(product.id)))
            total_price += (product.price * cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            print(order.id)
        display_amount = total_price
        total_price *= 100
        payment_order=client.order.create(dict(amount=total_price,currency='INR', payment_capture=1))
        payment_order_id=payment_order['id']
        request.session['cart'] = {}

        return render(request,'pay.html',{"api_key":RAZORPAY_API_KEY,"amount":total_price,"order_id":payment_order_id,"display_amount":display_amount})
