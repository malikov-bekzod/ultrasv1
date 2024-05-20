from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category,Product,Cart,Wishlist,Order,Brands
# Register your models here.


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ["id", "name", "created_date"]
    list_display_links = ["id", "name", "created_date"]
    search_fields = ["id", "name", "created_date"]
    ordering = ["id"]


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ["id", "name", "color","size","price","category","gender","description", "created_date"]
    list_display_links = [
        "id",
        "name",
        "color",
        "size",
        "price",
        "category",
        "gender",
        "description",
        "created_date",
    ]
    search_fields = [
        "id",
        "name",
        "color",
        "size",
        "price",
        "category",
        "gender",
        "description",
        "created_date",
    ]
    ordering = ["id"]


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ["id", "product","user","created_date"]
    list_display_links = ["id", "product","user","created_date"]
    search_fields = ["id", "product", "user", "created_date"]
    ordering = ["id"]


@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
    list_display = ["id", "product", "user", "created_date"]
    list_display_links = ["id", "product", "user", "created_date"]
    search_fields = ["id", "product", "user", "created_date"]
    ordering = ["id"]


@admin.register(Wishlist)
class WishlistAdmin(ImportExportModelAdmin):
    list_display = ["id", "product", "user", "created_date"]
    list_display_links = ["id", "product", "user", "created_date"]
    search_fields = ["id", "product", "user", "created_date"]
    ordering = ["id"]


@admin.register(Brands)
class BrandsAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]
    ordering = ["name"]
