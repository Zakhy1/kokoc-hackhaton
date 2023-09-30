from django.contrib import admin

from organisations.models import Organisation, Department


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ["title", "summary", "is_verified"]
    list_filter = ["is_verified"]
    search_fields = ["title"]
    readonly_fields = ["summary"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["title", "organisation"]
    list_filter = ["organisation"]
    search_fields = ["organisation"]
