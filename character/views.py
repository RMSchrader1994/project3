from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponseForbidden

# Create your views here.
@login_required(login_url='/accounts/login')
def character_list(request):
    characters = Character.objects.all()
    # can_edit = Post.author == request.user or request.user.is_staff
    return render(request, "character/character_list.html", {'characters': characters})
    
    
@login_required(login_url='/accounts/login')
def character_detail(request, id):
    characters = get_object_or_404(Character, pk=id)
    characters.save()
    return render(request, "character/character_detail.html", {'characters': characters})
    
def delete_character(request, id):
    characters = get_object_or_404(Character, pk=id)
    characters.delete()
    return redirect("character_list")
    
@login_required(login_url='/accounts/login')
def create_characters(request):
    if request.method=="POST":
        form = CharacterForm(request.POST, request.FILES)
        characters = form.save(commit=False)
        characters.author = request.user
        characters.save()
        return redirect('character_list')
    else:
        form = CharacterForm()
    characters = CharacterForm()
    return render(request, "character/create.html", { 'form': form, 'characters': characters})
    
@login_required(login_url='/accounts/login')
def edit_character(request, id): 
    characters = get_object_or_404(Character, pk=id)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=characters)
        if form.is_valid():
            form.save()
            return redirect("character_list")
    else:
        print("It's the GET")
        
    form = CharacterForm(instance=characters)
    return render(request, "character/edit.html", {'form': form})