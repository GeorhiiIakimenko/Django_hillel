from django.contrib import admin
from .models import Category, Goods, Tag


class MyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'active', 'review', 'sale', 'company', 'image']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']
    list_filter = ['id', 'name', 'price', 'active', 'sale', 'company']


class GoodsAdminInLine(admin.StackedInline):
    model = Goods.tags.through
    extra = 2


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    inlines = [GoodsAdminInLine]


admin.site.register(Category)
admin.site.register(Goods, MyAdmin)
admin.site.register(Tag, TagAdmin)
