from django.contrib import admin
from .models import AppUser

# Register your models here.

class AppUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(AppUser, AppUserAdmin)