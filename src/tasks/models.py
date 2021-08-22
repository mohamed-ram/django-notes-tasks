from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.db import models

from categories.models import Category
from utils.receivers import slug_pre_save_receiver, user_pre_save_receiver
from utils.current_request import request

User = get_user_model()

# task query set.
class TaskQueryset(models.QuerySet):
    def all(self):
        req = request()
        return self.filter(user=req.user)
    
    def completed(self):
        return self.filter(completed=True)
    
    def uncompleted(self):
        return self.filter(completed=False)


# task manager.
class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQueryset(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().all()
    
    def completed(self):
        return self.get_queryset().completed()
    
    def uncompleted(self):
        return self.get_queryset().uncompleted()


# main task class.
class Task(models.Model):
    # priority choices.
    class PriorityChoices(models.TextChoices):
        LOW = "A", "low"
        MEDIUM = "B", "medium"
        HIGH = "C", "high"
    
    # other fields.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=PriorityChoices.choices, default=PriorityChoices.LOW)
    
    objects = TaskManager()
    
    class Meta:
        ordering = ['-priority', '-timestamp']
    
    
    def __str__(self):
        return self.title


pre_save.connect(slug_pre_save_receiver, sender=Task)
pre_save.connect(user_pre_save_receiver, sender=Task)
