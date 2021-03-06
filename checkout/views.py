from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import *
from decimal import Decimal
from cart.utils import get_cart_items
from django.utils import timezone
from .models import OrderLineItem
from django.conf import settings
import stripe
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

@login_required(login_url='/accounts/login')
def checkout(request):

    if request.method=="POST":
        
        order_form = OrderForm(request.POST)
        order = order_form.save(commit=False)
        order.date = timezone.now()
        
        order.save()
        
        cart = request.session.get('cart', {})
        for id, quantity in cart.items():
            product = get_object_or_404(DLC, pk=id)
            order_line_item = OrderLineItem (
                order = order,
                product = product,
                quantity = quantity
                )
            order_line_item.save()
            payment_form = MakePaymentForm(request.POST)
            if payment_form.is_valid():
                
                total = get_cart_items(cart)['total']
                total_in_cent = int(total * 100)
                
                try:
                    customer = stripe.Charge.create(
                    amount= total_in_cent,
                    currency="EUR",
                    description="Dummy Transaction",
                    card=payment_form.cleaned_data['stripe_id']
                    )
                    if customer.paid:
                        messages.error(request, "You have successfully paid")
                    
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")
                    
        del request.session['cart']
        return redirect("get_dlc")
    
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        
        context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY }
        
        cart = request.session.get('cart', {})
        cart_items_and_total = get_cart_items(cart)
        
        context.update(cart_items_and_total)
    
    return render(request, "checkout/checkout.html", context)
    

