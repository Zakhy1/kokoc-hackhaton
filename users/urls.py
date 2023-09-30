from django.urls import path, include

from events import views

app_name = "users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    # path("register/", views.register, name="register"),
    # path("edit/", views.edit, name="edit"),
]
