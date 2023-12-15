from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('USER', 'Usuario'),
        ('GUEST', 'Invitado'),
    ]

    rol = models.CharField(max_length=5, choices=ROLES, default='USER')

    def __str__(self):
        return self.username
