from django.urls import include, path

urlpatterns = [
    path("coin/", include(("src.coin.urls", "coin"), namespace="coin")),
    # path("order/", include(("src.authentication.urls", "authentication"))),
    # path("user/", include(("src.user.urls", "user"))),
]
