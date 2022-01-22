from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class User(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    list_editable = ('is_active', 'is_staff', 'is_superuser')
