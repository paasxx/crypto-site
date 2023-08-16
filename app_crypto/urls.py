from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("market_data/<crypto>", views.market, name="market"),
    path("plot/<crypto>", views.plot, name="plot"),
    path("json/", views.post_json, name="json"),
    path("spinner/", views.test, name="test"),
]
