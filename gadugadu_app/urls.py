from django.urls import path

from gadugadu_app.views import *

urlpatterns = [
    path('', show_messages),
    path('gg/form/', ShowFormView.as_view()),
]