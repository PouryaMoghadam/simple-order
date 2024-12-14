from django.urls import path

from .views import (
    coin_list_view,
)

app_name = "coin"


urlpatterns = [
    path("", coin_list_view, name="coin_list_view"),
]
