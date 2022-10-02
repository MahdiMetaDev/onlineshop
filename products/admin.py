from django.contrib import admin

from .models import Product, Comment


class CommentInline(admin.TabularInline):    # we also have StackedInline
    """
    This is for each product comments separately
    """
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]
    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active', ]

