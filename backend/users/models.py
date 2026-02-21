from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = "client", "Client"
        DOCTOR = "doctor", "Doctor"
        PHARMACY = "pharmacy", "Pharmacy"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CLIENT)