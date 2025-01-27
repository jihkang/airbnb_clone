from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """ custom user admin pannel """

    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    pass