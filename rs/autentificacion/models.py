from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nickname = models.ForeignKey(User, blank=False, null=False)
    nombre = models.CharField(blank=False, null=False, max_length=50)
    apellido = models.CharField(blank=False, null=False, max_length=50)
    correo  = models.EmailField(blank=False, null=False, max_length=50)
    edad = models.CharField(blank=False, null=False, max_length=50)
    genero = models.CharField(blank=False, null=False, max_length=50)
    contra = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return "perfil de {}".format(self.nombre)
