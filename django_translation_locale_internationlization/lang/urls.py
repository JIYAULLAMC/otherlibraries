from django.urls import path, include
from . import views
from django.utils.translation import gettext as _

app_name = "lang"

urlpatterns = [
    path("", views.home, name="home"),
]
