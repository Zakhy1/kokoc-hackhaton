from django.contrib import admin

from organisations.models import Fund
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "is_boss"]
    search_fields = ["email"]
    ordering = ["id"]


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ["title", "donated"]
    list_filter = ["title"]
    search_fields = ["title"]
    readonly_fields = ["donated"]
