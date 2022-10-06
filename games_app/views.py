from django.shortcuts import render, redirect
from django.views import View
from games_app.models import *


def games_list(request):
    if request.method == "GET":
        games = Game.objects.all()
        return render(request, 'games_app/index.html', context={'games': games})

def show_game(request, pk):
    if request.method == "GET":
        game = Game.objects.get(pk=pk)
        return render(request, 'games_app/show.html', context={'game': game})

def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'games_app/edit.html', context={'game': game})
    if request.method == "POST":
        new_name = request.POST.get('name')
        new_desc = request.POST.get('desc')
        new_rating = request.POST.get('rating')
        new_price = request.POST.get('price')
        new_platform = request.POST.get('platform')
        game.name = new_name
        game.platform_id = Platform.objects.get(name=new_platform).pk
        game.description = new_desc
        game.rating = new_rating
        game.price = new_price
        game.save()
        return redirect('../')

def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'games_app/delete.html', context={'game': game})
    if request.method == "POST":
        option = request.POST.get('option')
        if option == 'nie':
            return redirect('../')
        if option == 'tak':
            game.delete()
            return redirect('../')

def add_game(request):
    if request.method == 'GET':
        return render(request, 'games_app/add_form.html')
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_platform = request.POST.get('platform')
        new_desc = request.POST.get('desc')
        new_rating = request.POST.get('rating')
        new_price = request.POST.get('price')
        if request.POST.get('platform') == '':
            new_platform = None
            Game.objects.create(name=new_name,
                                description=new_desc,
                                rating=new_rating,
                                price=new_price,
                                platform_id=new_platform
                                )
        else:
            Game.objects.create(name=new_name,
                                description=new_desc,
                                rating=new_rating,
                                price=new_price,
                                platform_id=Platform.objects.get(name=new_platform).pk
                                )
        return redirect('../')

def platform_list(request, pk):
    if request.method == 'GET':
        platform = Platform.objects.get(pk=pk)
        games = platform.game_set.all()
        return render(request, 'games_app/platform.html', context={'platform': platform, 'games': games})
