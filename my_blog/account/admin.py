from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .form import CustomUserCreationForm , CustomUserChangeForm
from account .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','age']
    model = CustomUser

admin.site.register(CustomUser,CustomUserAdmin)