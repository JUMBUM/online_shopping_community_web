from django.shortcuts import render
from django.http import HttpResponse

import cartapp.model_df.cart as cart
# Create your views here.

def test(request):
    return HttpResponse('<u>Hello</u>')
    
def cart_main(request) :
    df = cart.get_pay()
    
    context = {"df" : df.to_html}
    
    return render(request,
                    "cartapp/cart/01_cart.html",
                    context) 

def cart_main2(request) :
    df = cart.get_pay2()
    #c_list = cart.get_cartlist()
    #context = {"df" : df}
    return render(request,
                    "cartapp/cart/02_cart.html",
                    df) 
    
def cart_list(request) :
    df = cart.get_cartlist()
    
    context = {"df" : df}
    
    return render(request,
                    "cartapp/cart/02_cart.html",
                    context) 