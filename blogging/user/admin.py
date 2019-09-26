from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserChangeForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "age", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)