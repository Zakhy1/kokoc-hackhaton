from django.contrib import admin

from events.models import Activity, Period, Event, EventProof


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(EventProof)
class EventProofAdmin(admin.ModelAdmin):
    list_display = ["user", "event", "сonfirmed"]
    list_filter = ["user", "event"]
    search_fields = ["user"]


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ["start", "end"]
    list_filter = ["start", "end"]
    ordering = ["start"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "activity", "period"]
    list_filter = ["price", "period"]
    search_fields = ["title"]
