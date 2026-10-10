from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('CLIENT', 'Client'),
        ('FREELANCER', 'Freelancer'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    bio = models.TextField(
        blank=True
    )

    skills = models.CharField(
        max_length=500,
        blank=True
    )