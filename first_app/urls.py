from django.urls import path

from first_app.views import *

urlpatterns = [
    path('hello_name/', hello_name),
    path('add/', add),
    path('multiply/', multiply),
    path('brothers/', brothers),
    path('fibonacci/', fibonacci),
    path('game/', game),
    path('hello/<str:name>/', hello_path),
    path('article/<int:id>/', article),
    path('greetings/<str:name>/<int:repeat>/', greetings),
    path('calc/<int:number_a>/<path:operation>/<int:number_b>/', calc),
    path('random/<int:min>/<int:max>/', random_generator),
    path('random/<int:min>/<int:max>/<int:throw>/', random_generator),
    path('', index),
    path('form/', form),
    path('fizz/<int:n>/', fizz),
    path('bmultiply/<int:n>/', multiply_template),
    path('rpggame/', rpg_game),
    path('messages/', list_messages),
    path('comments/', list_comments),
    path('main/', main),
    path('login/', login_user),
    path('login/<str:message>', login_user),
    path('add_product/', add_product),
    path('product/show/', show_products),
    path('view/', FormView.as_view()), # widoki klas .as_view() !!!!
    path('pizza/', PizzaView.as_view()),
    path('car/', CarView.as_view()),
]