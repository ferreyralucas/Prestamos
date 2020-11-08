from django.contrib import admin
from django.contrib.auth.models import User
from .models import  Prestamo
# Register your models here.

admin.site.register(Prestamo)

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    actions_on_top = True