from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


User = settings.AUTH_USER_MODEL

def upload_avatar(instance, filename):
    extension = filename.split(".")[-1]
    return f"{instance.user.username}-avatar.{extension}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(default='avatar.png', upload_to=upload_avatar)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

