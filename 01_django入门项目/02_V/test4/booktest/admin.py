from django.contrib import admin
from booktest.models import Blog
# Register your models here.

@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','read']
    ordering = ['id']
