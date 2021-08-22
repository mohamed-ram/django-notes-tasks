from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save

from utils.receivers import slug_pre_save_receiver, user_pre_save_receiver
from utils.current_request import request

User = get_user_model()


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


pre_save.connect(user_pre_save_receiver, sender=Category)
pre_save.connect(slug_pre_save_receiver, sender=Category)
