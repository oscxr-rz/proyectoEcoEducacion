from django.db import models
from app_juegos.models import Usuario

class Pregunta(models.Model):
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuesta')
    correcta = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tiempo_respuesta = models.FloatField(default=0)

    def __str__(self):
        return f"Respuesta a {self.pregunta.texto} por {self.usuario.nombre}"


