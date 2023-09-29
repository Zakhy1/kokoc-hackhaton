from django.contrib import admin

from organisations.models import Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ["title", "summary", "is_verified"]
    list_filter = ["is_verified"]
    search_fields = ["title"]
    
