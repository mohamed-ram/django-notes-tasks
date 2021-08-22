from django.utils.text import slugify
from .current_request import request

def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)



def user_pre_save_receiver(sender, instance, *args, **kwargs):
    req = request()
    instance.user = req.user


