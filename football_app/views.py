from django.shortcuts import render, redirect
from django.views import View

from football_app.forms import FootballForm, TeamForm
from football_app.models import Team, Game


# Create your views here.

class AddTeam(View):
    def get(self, request):
        form = TeamForm()
        return render(request, 'football_app/football_form.html', {'form': form, 'message': 'dodaj'})

    def post(self, request):
        form = TeamForm(request.POST, instance=Team())
        if form.is_valid():
            form.save()
            return redirect('/football/')
        else:
            return render(request, 'football_app/football_form.html', {'form': form, 'message': 'dodaj'})

class AddGame(View):
    def get(self, request):
        form = FootballForm()
        return render(request, 'football_app/football_form.html', {'form': form, 'message':'dodaj'})

    def post(self, request):
        form = FootballForm(request.POST, instance=Game())
        if form.is_valid():
            form.save()
            return redirect('/football/')
        else:
            return render(request, 'football_app/football_form.html', {'form': form, 'message': 'dodaj'})

def show_matches(request):
    games = Game.objects.all()
    return render(request, 'football_app/index.html', {'games': games})
