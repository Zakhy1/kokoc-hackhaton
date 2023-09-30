from django.urls import path

from organisations import views

app_name = "organisations"

urlpatterns = [
    path("register-fund", views.register_fund, name="reg_fund"),
    path("register-org", views.register_organisation, name="reg_org"),
]
