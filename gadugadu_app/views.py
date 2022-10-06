from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from gadugadu_app.forms import LoginForm
from gadugadu_app.models import Message


# Create your views here.

def show_messages(request):
    messages = Message.objects.all()
    return render(request, 'gadugadu_app/messages.html', context={'messages': messages})

class ShowFormView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'gadugadu_app/loginform.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get("login")
            password = form.cleaned_data.get("password")
            return HttpResponse(f"Zalogowano {login}, twoje hasło {password}") # zapisz bane do dazy, zalogowac uzytkownika
        else:
            return render(request, 'gadugadu_app/loginform.html', context={'form': form})
