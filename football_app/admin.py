from django.contrib import admin

from football_app.models import Team, Game

# Register your models here.

admin.site.register(Team)
admin.site.register(Game)