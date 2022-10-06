from django.urls import path

from football_app.views import AddGame, AddTeam, show_matches

urlpatterns = [
    path('add_team', AddTeam.as_view()),
    path('add_match/', AddGame.as_view()),
    path('', show_matches),
]