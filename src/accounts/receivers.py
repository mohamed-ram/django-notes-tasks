from profiles.models import Profile


def post_save_profile_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

