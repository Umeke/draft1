from django.contrib import admin
from .models import Shop, Category, Product


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop_name')


admin.site.register(Shop, ShopAdmin)


class CategoryAdmin(admin.ModelAdmin):
    filter = ('shop',)
    list_display = ('id', 'cat_name', 'shop_name')


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    filter = ('shop',)
    list_display = ('id', 'product_name','cat_name', 'shop_name')


admin.site.register(Product, ProductAdmin)