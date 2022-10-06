from django.shortcuts import render, redirect
from django.views import View

from library_app.forms import BookForm
from library_app.models import Book


# Create your views here.

class AddBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'library_app/book_form.html', context={'form': form, 'message': 'Dodaj książkę'})

    def post(self, request):
        form = BookForm(request.POST, instance=Book())
        if form.is_valid():
            form.save()
            return redirect('/lib/')
        else:
            return render(request, 'library_app/book_form.html', context={'form': form, 'message': 'Dodaj książkę'})

class EditBookView(View):
    def get(self, request, pk):
        form = BookForm(instance=Book.objects.get(pk=pk))
        return render(request, 'library_app/book_form.html', context={'form': form, 'message': 'Edytuj książkę'})
    def post(self, request, pk):
        form = BookForm(request.POST, instance=Book.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('/lib/')
        else:
            return render(request, 'library_app/book_form.html', context={'form': form, 'message': 'Edytuj książkę'})
