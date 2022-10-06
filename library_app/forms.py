from django import forms

from library_app.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__' #['title', 'author']
