from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_boss"]
    search_fields = ["username", "email"]
    ordering = ["id"]
