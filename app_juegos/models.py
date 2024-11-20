from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Puntuacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    quiz = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.usuario.nombre} - quiz: {self.quiz}"


