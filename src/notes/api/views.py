from rest_framework import generics
from .serializers import NoteSerializer
from ..models import Note

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'slug'

