from django.db import models

class Contact(models.Model):
    Nombre=models.CharField(max_length=25)
    email=models.EmailField()
    telefono=models.CharField(max_length=12)
    descripcion=models.TextField()

    def __str__(self):
        return self.email

