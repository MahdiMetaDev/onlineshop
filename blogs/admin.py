from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class CustomBlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', ]
