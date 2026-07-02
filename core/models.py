from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.CharField('E-mail', max_length=200, unique=True)
    # profile_pic = models.ImageField( upload_to='perfil/', null=True, blank=True)
    def __str__(self):
        return self.email