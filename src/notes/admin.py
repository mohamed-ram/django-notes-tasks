from django.contrib import admin

from .forms import NoteForm
from .models import Note

# customize admin page.
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp']
    search_fields = ['title', 'content']
    form = NoteForm
    
    # def get_queryset(self, request):
    #     return Note.objects.all()


admin.site.register(Note, NoteAdmin)

