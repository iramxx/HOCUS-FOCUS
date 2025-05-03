from django.urls import path
<<<<<<< HEAD
from . import views

app_name = "vllmpage"

urlpatterns = [
    path("", views.home, name="home"),  
    path("game/", views.game, name="game"),
]
=======

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
]
>>>>>>> cb7d6eb039053ecdecc18900e4594511fef411ef
