from django.contrib import admin
from .models import Category, Blog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'published', 'created_at')
    list_filter = ('published', 'category')
    search_fields = ('title', 'content')
