from django.contrib import admin

from games_app.models import Game, Platform, Category, GameDetails

# Register your models here.

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Category)
admin.site.register(GameDetails)
