from django.urls import path
from . import views

app_name = "vllmpage"

urlpatterns = [
    path("", views.home, name="home"),  
    path("game/", views.game, name="game"),
]
