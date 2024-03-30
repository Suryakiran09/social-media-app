from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        username = f"{instance.username}_profile"
        profile, created = Profile.objects.get_or_create(
            user=instance,
            defaults={"username": username}
        )
        if not created:
            profile.username = generate_unique_username(username)
            profile.save()

def generate_unique_username(base_username):
    counter = 1
    while True:
        username = f"{base_username}_{counter}"
        if not Profile.objects.filter(username=username).exists():
            return username
        counter += 1

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()