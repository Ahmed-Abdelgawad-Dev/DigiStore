from django.contrib import admin
from .models import Category, Product


admin.site.register(Category)

class CustomAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Product, CustomAdmin)
