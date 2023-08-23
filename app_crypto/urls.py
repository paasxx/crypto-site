from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("market_data/<crypto>", views.market, name="market"),
    path("plot/<crypto>", views.plot, name="plot"),
    path("update_database/", views.update_database, name="update_database"),
    path("update/", views.update, name="update"),
]
