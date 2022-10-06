from django.urls import path

from games_app.views import *

urlpatterns = [
    path('', games_list),
    path('show/<int:pk>', show_game),
    path('edit/<int:pk>', edit_game),
    path('delete/<int:pk>', delete_game),
    path('add/', add_game),
    path('platform/<int:pk>', platform_list),
]
