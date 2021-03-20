from django.db import models

# Create your models here.


class usuarios(models.Model):
    nombre = models.CharField(max_length=32, null=False)
    apellido = models.CharField(max_length=32, null=False)
    correo = models.EmailField(null=False)
    password = models.CharField(max_length=32, null=False)
    fecha_nacimiento = models.DateField(null=False)

    def __str__(self):
        return self.nombre+' '+self.apellido
