from django.contrib import admin

# Register your models here.

from .models import Film, Category

admin.site.register(Film)
admin.site.register(Category)