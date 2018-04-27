from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required(login_url='/accounts/login')
def get_dlc(request):
    product = DLC.objects.all()
    return render( request, "products/dlc.html", {'product': product})
