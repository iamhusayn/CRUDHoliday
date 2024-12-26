from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('books/', views.view_books),
  path('cart/', views.cart),
  path('save/', views.save_user),
]