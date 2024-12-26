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
    user_name = request.POST['user_name']
    return HttpResponse(f"Hi {user_name}, welcome to your Libary!")