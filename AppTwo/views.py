from django.shortcuts import render
from django.http import HttpResponse

# CRUD operations for different models. Examples:
# : Manage data related to "Authors" (fields: name, bio, date_of_birth, etc.).
# Create your views here.

def authors(request):
  return HttpResponse("Welcome to the author's page.") 
