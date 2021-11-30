from django.db import models

# Create your models here.
class Mensajes(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    self = models.CharField(max_length=200)