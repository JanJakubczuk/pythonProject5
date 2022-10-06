from django.urls import path

from library_app.views import AddBookView, EditBookView

urlpatterns = [
    path('add/', AddBookView.as_view()),
    path('edit/<int:pk>', EditBookView.as_view()),
]