from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("market_data/<crypto>", views.market, name="market"),
]
