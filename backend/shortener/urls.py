from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view),
    path("dashboard/", views.dashboard),
    path("shorten/", views.shorten),
    path("<str:code>", views.redirect_url),
]
