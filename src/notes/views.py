from django.db.models import Q
from django.shortcuts import render
from .models import Note


def note_list(request):
    notes = Note.objects.all()
    
    query = request.GET.get('query', None)
    if query:
        notes = notes.filter(Q(title_icontains=query) | Q(content_icontains=query))
    
    context = {
        "notes": notes,
        "count": notes.count(),
    }
    return render(request, 'notes/note_list.html', context=context)

