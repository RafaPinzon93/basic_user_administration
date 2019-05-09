import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from internationalflavor.iban import IBANField

from social_django.models import UserSocialAuth


class User(AbstractUser):
    iban = IBANField()
    created_by = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name="users", blank=True, null=True)


@receiver(pre_save, sender=User)
def assign_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = uuid.uuid4().hex[:30]


@receiver(post_save, sender=UserSocialAuth)
def set_adiminstrator_for_user(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.is_staff = True
        user.save()
