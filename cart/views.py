from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import DLC
from decimal import Decimal
from cart.utils import get_cart_items

@login_required(login_url='/accounts/login')
def view_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items(cart)
    return render(request, "cart/view_cart.html", context)
    

def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('get_dlc')



def delete_product(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart')