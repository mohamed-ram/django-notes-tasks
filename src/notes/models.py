from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save

from utils.current_request import request
from utils.receivers import user_pre_save_receiver, slug_pre_save_receiver
from categories.models import Category
from utils.helper_functions import upload_notes_to
User = get_user_model()

# note query set.
class NoteQuerySet(models.QuerySet):
    # def all(self):
    #     req = request()
    #     return self.filter(user=req.user)
    pass

# note model manager.
class NoteManager(models.Manager):
    def get_queryset(self):
        return NoteQuerySet(self.model, using=self._db)
    
    # def all(self):
    #     return self.get_queryset().all()
        

# main note model.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', blank=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_notes_to)
    content = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')
    
    objects = NoteManager()
    
    class Meta:
        ordering = ['-timestamp']
    
    
    def __str__(self):
        return self.title


# pre save functionalities.
pre_save.connect(user_pre_save_receiver, sender=Note)
pre_save.connect(slug_pre_save_receiver, sender=Note)


