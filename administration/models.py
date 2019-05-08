from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    iban = models.CharField(max_length=34)
    created_by = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name="users", blank=True, null=True)
