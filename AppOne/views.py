from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AddBooks

# CRUD operations for different models. Examples:
# : Manage data related to "Books" (fields: title, author, publication_date, etc.).
# Create your views here.
def home(request): 
    return render(request,"index.html",context={})

def view_books(request):
    return HttpResponse("Welcome to your cart. What books will you like to add?")

def cart(request):
    return HttpResponse("My selected books are stroed here")

def save_user(request):
    users_name = request.POST['users_name']
    return render(request,"welcome.html",context={'users_name':users_name})