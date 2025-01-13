from django.contrib import admin
from .models import AddBooks

# Register your models here.
class AppOneAdmin(admin.ModelAdmin):
  list_display = ('Tittle', 'Author', 'Field', 'Status', 'Published', 'Rating')
  search_fields = ('Tittle', 'Author', 'Field', 'Status', 'Published', 'Rating')

  # admin.site.register(AddBooks, AppOneAdmin)