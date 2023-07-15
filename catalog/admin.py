from django.contrib import admin
from .models import Category, Goods


class MyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'active', 'review', 'sale', 'company']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']
    list_filter = ['id', 'name', 'price', 'active', 'sale', 'company']


admin.site.register(Category)
admin.site.register(Goods, MyAdmin)
