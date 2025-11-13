from django.db import models

class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} | {self.fecha_lanzamiento}'


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'
    

class Review(models.Model):

    class Puntaje(models.IntegerChoices):
        CERO = 0, '0'
        UNO = 1, '1'
        DOS = 2, '2'
        TRES = 3, '3'
        CUATRO = 4, '4'
        CINCO = 5, '5'
        SEIS = 6, '6'
        SIETE = 7, '7'
        OCHO = 8, '8'
        NUEVE = 9, '9'
        DIEZ = 10, '10'

    juego = models.ForeignKey(Juego, on_delete=models.PROTECT, related_name='reseñas')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='reseñas')
    
    puntaje = models.IntegerField(choices=Puntaje.choices, default=Puntaje.CERO)
    comentario = models.TextField(max_length=1000)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.juego} ({self.puntaje})"

