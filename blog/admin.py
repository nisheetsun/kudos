from django.contrib import admin
from .models import Blog, Content

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    pass

class ContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Content, ContentAdmin)