from django import forms

from football_app.models import Team, Game

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class FootballForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

