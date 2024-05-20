from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ["id","title", "text", "author","topic","created_date"]
    list_display_links = ["id","title", "text", "author","topic","created_date"]
    search_fields = ["id","title", "text", "author","topic","created_date"]
    ordering = ["id"]
