from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, nombre, apellido, password, correo, fecha_nacimiento, **extra_fields):
        user = self.model(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            fecha_nacimiento=fecha_nacimiento,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, nombre, apellido, password, correo, fecha_nacimiento, **extra_fields):
        user = self._create_user(
            nombre, apellido, password, correo, fecha_nacimiento)
        return user
