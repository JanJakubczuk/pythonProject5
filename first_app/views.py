from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

from django.views import View

from first_app.fake_data import *
number = random.randint(1, 100)
products = {}

def hello(request):
    return HttpResponse('Hello')


def hello_name(request):
    name = request.GET.get('name', 'nieznajomy')
    return HttpResponse('Witaj ' + name)


def add(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return HttpResponse(f"Bledne dane")
    return HttpResponse(a + b)


def multiply(request):
    n = request.GET.get('n')
    try:
        n = int(n)
    except ValueError:
        n = 3

    multiply_tab = '<table border=1>'
    for i in range(1, n + 1):
        multiply_tab += f'<tr>'
        for j in range(1, n + 1):
            multiply_tab += f'<td style="padding: 10px; color: red; border: 1px solid black">{i * j}</td>'
    multiply_tab += f"</tr></table>"

    return HttpResponse(multiply_tab)


def brothers(request):
    names = request.GET.getlist('names')
    response = ""
    i = 0
    for name in names:
        i += 1
        if i % 2 == 0:
            response += f'<p style="background:yellow">{name}</p>'
        else:
            response += f'<p>{name}</p>'

    return HttpResponse(response)


def fibonacci(request):
    n = int(request.GET.get('n'))
    response = "<ol>"
    a, b = 0, 1
    while n > 1:
        response += f'<li>{b}</li>'
        a, b = b, a + b
        n -= 1
    response += "</ol>"
    return HttpResponse(response)

def game(request):
    message = ''
    guess = 0
    try:
        guess = int(request.GET.get('guess'))
    except:
        pass

    if guess < number:
        message = "za mala"
    elif guess > number:
        message = "za duza"
    else:
        message = "zgadles"

    response = '<form><input name="guess" placeholder="podaj liczbe(1-100)"></form>'
    response += message
    return HttpResponse(response)

def hello_path(request, name):
    return HttpResponse(name)

def article(request, id):
    match id:
        case 1:
            return HttpResponse("abc")
        case 2:
            return HttpResponse("def")
        case 3:
            return HttpResponse("inna")

    if id > 3:
        return HttpResponse("brak artykulu o podanym id")

def greetings(request, name, repeat):
    response = ''
    for x in range(repeat):
        response += f'Witaj {name} <br>'

    return HttpResponse(response)

def calc(request, number_a, operation, number_b):
    try:
        if operation == "plus":
            return HttpResponse(number_a + number_b)
        elif operation == "minus":
            return HttpResponse(number_a - number_b)
        elif operation == "multiply":
            return HttpResponse(number_a * number_b)
        elif operation == "divide":
            return HttpResponse(number_a / number_b)
        else:
            return HttpResponse("nie mogę wykonać tej operacji")
    except ValueError:
        return HttpResponse('nieprawidlowe dane')
    except TypeError:
        return HttpResponse('nieprawidlowe dane')

def random_generator(request, min, max, throw=1):
    response = 0
    for x in range(throw):
        response += random.randint(min, max)

    return HttpResponse(response)

# templates

def index(request):
    return render(request,
                  'first_app/index.html',
                  context={'message': 'Wiadomość z szablonu',
                           'names': ['Jan', 'Adam', 'Piotr', 'Ola']})

def form(request):
    if request.method == 'GET':
        return render(request, 'first_app/form.html')
    if request.method == 'POST':
        return HttpResponse(request.POST.get('test', 'brak parametru'))

def fizz(request, n):
    fizz_buzz = []
    for x in range(1, n + 1):
        if x % 3 != 0 and x % 5 != 0:
            fizz_buzz.append(x)
        elif x % 3 == 0 and x % 5 != 0:
            fizz_buzz.append('Fizz')
        elif x % 3 != 0 and x % 5 == 0:
            fizz_buzz.append('Buzz')
        else:
            fizz_buzz.append('Fizz Buzz')
    return render(request,
                  'first_app/fizz_buzz.html',
                  context={'data': fizz_buzz})

def multiply_template(request, n):
    data = []
    for i in range(1, n + 1):
        data.append(i)

    return render(request,
                  'first_app/multiply.html',
                  context={'elements': data})

def rpg_game(request):
    player_hp = random.randint(100, 200)
    enemy_hp = random.randint(100, 500)
    default = []
    default.append(player_hp)
    default.append(enemy_hp)
    player_damage1 = 10
    enemy_damage1 = 10
    turn = 1
    elements = ''
    result = ''
    while player_hp > 0 and enemy_hp > 0:
        player_damage = random.randint(100, 300)
        enemy_hp -= player_damage
        enemy_damage = random.randint(100, 300)
        player_hp -= enemy_damage

        elements += f'Tura {turn}<br>'
        elements += f'Player attack <br> Enemy lost {player_damage}<br>'
        elements += f'Enemy hp {enemy_hp}<br>'
        elements += f'Enemy attack <br> Player lost {enemy_damage}<br>'
        elements += f'Player hp {player_hp}<br>'
        turn += 1
        if player_hp < 1 and enemy_hp > 0:
            result = 'GAME OVER – you LOSE'
        elif enemy_hp < 1 and player_hp > 0:
            result = 'NEXT LEVEL – you WIN'
        if player_hp <= 0 and enemy_hp <= 0:
            if player_hp > enemy_hp:
                result = 'NEXT LEVEL – you WIN'
            else:
                result = 'GAME OVER – you LOSE'
    return render(request,
                  'first_app/rpg_game.html',
                  context={'elements': elements,
                           'def_p_damage': player_damage1,
                           'def_e_damage': enemy_damage1,
                           'def_hp_p': default[0],
                           'def_hp_e': default[1],
                           'result': result})


def list_messages(request):
    messages = [
        "pierwsza wiadomosc",
        "druga wiadomosc",
        "trzecia wiadomosc"
    ]

    return render(request, 'first_app/list_message.html', {"messages": messages})

def list_comments(request):
    return render(request, 'first_app/list_comment.html', {'comments': fake_comments})

def main(request):
    return render(request, 'first_app/main.html')

def login_user(request):
    if request.method == "GET":
        return render(request, 'first_app/login.html')
    if request.method == "POST":
        if request.POST.get('user') == 'Admin' and request.POST.get('passw') == 'Tajne123':
            return HttpResponse('Witaj Admin!')
        else:
            return redirect('../login/?message=zly login lub haslo')

def add_product(request):
    if request.method == 'GET':
        return render(request, 'first_app/add_product_form.html')
    if request.method == 'POST':
        product = request.POST.get('product')
        price = request.POST.get('price')
        products[product] = price
        return redirect('../product/show')

def show_products(request):
    return render(request, 'first_app/product_show.html', context={'products': products})

# klasy widokow

class FormView(View):
    def get(self, request):
        return HttpResponse("Metoda GET")
    def post(self, request):
        return HttpResponse("Metoda POST")

class PizzaView(View):
    def get(self, request):
        return render(request, 'first_app/pizza.html')
    def post(self, request):
        skladnik = request.POST.getlist('skladnik')
        return HttpResponse(", ".join(skladnik))

class CarView(View):
    def get(self, request):
        return render(request, 'first_app/car.html')
    def post(self, request):
        cars = request.POST.getlist('cars')
        return HttpResponse(", ".join(cars))

class LoginView(View):
    def get(self, request):
        return render(request, 'first_app/login_class.html')
    def post(self, request):
        login = request.POST.get('login')
        passw = request.POST.get('passw')

