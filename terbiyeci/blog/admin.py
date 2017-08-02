from copy import copy
from django.contrib import admin

# Register your models here.


# ShortNews
# Category
from django.contrib.auth.admin import UserAdmin

from blog.models import Category, ShortNews, User


class ShortNewsCategoryInline(admin.TabularInline):
    model = ShortNews.categories.through
    extra = 0


class ShortNewsChildrenInline(admin.StackedInline):
    model = ShortNews
    extra = 0


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Extra", {"fields": ("biography",)}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]
    inlines = [ShortNewsCategoryInline]


@admin.register(ShortNews)
class ShortNewsAdmin(admin.ModelAdmin):
    inlines = [ShortNewsChildrenInline]  # Detay ekranında ek model verileri
    list_display = [  # Liste ekranında gösterilecek sütunlar
        "title",
        "created",
        "score",
        "report_count",
        "categoryname",
        "hidden"
    ]
    search_fields = [  # Liste ekranında aranılacak sütunlar
        "title",
        "source",
        "slug",
    ]
    list_filter = [  # Liste ekranında filtrelenecek sütunlar
        "created",
        "featured_for",
        "score",
        "report_count",
        "categories",
    ]

    fieldsets = [
        (
            "Global",
            {
                "fields": [
                    ("title", "slug"),
                    ("score", "report_count"),
                    "source",
                    "image",
                    "categories",
                    "parent_news",
                    "hidden"
                ]

            }
        ),
        (
            "Dates",
            {
                "fields": [
                    ("created", "featured_for"),
                ]
            }
        ),
    ]

    def categoryname(self, object):
        names = []
        for obj in object.categories.all():
            names.append(obj.name)
        if names:
            return ", ".join(names)
        else:
            return ""