from django.shortcuts import render
from django.http import HttpResponse

# CRUD operations for different models. Examples:
# : Manage data related to "Books" (fields: title, author, publication_date, etc.).
# Create your views here.
def welcome(request):
    return HttpResponse("Hi, Welcome to Books Hub!")
