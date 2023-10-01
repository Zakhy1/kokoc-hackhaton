from django.urls import path

from events import views

app_name = "events"

urlpatterns = [
    path("", views.index, name="index"),
    path("activities/", views.activities, name="activities"),
    path("participate/<int:event_id>", views.participate, name="participate"),
    path("proof/<int:event_id>", views.confirm_event, name="proof")
]
