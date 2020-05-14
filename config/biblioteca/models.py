from django.db import models

# Create your models here.
class Autor (models.Model):
    nombre = models.Charfield(max_length = 20)

class Libro(models.Model):
    titulo = models.Charfield(max_length = 20)
    editorial = models.Charfield(max_length = 20)
    paginas = models.Charfield(max_length = 20)
    autor = models.ForeignKey("Autor", on_delete=models.CASCADE,null = False,)
