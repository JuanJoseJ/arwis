from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

# Create your models here.

# modelo de usuario con la info solicitada
class usuarios(AbstractBaseUser):
    nombre = models.CharField(max_length=32, null=False)
    apellido = models.CharField(max_length=32, null=False)
    correo = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=200, null=False)
    fecha_nacimiento = models.DateField(null=False)

    USERNAME_FIELD = 'correo'

    objects = UserManager()

    def __str__(self):
        return self.correo+' '+self.nombre+' '+self.apellido
