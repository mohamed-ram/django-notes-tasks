from django.urls import path
from . import views

urlpatterns = [
    path('note_list', views.NoteListCreate.as_view()),
    path('note_list/<str:slug>', views.NoteDetailView.as_view()),
]
