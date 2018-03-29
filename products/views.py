from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def get_dlc(request):
    product = DLC.objects.all()
    return render( request, "products/dlc.html", {'product': product})
    
def create_post(request):
    if request.method=="POST":
        form = DLCForm(request.POST, request.FILES)
        product = form.save(commit=False)
        product.save()
        return redirect("get_dlc")
    else:
        form = DLCForm()
    items = DLCForm()
    return render(request, "products/create_item.html", { 'form': form, 'items': items})
    
def product_item(request, id):
    product = get_object_or_404(DLC, pk=id)
    return render(request, "products/product_item.html", {'product': product})