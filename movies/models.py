from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.TextField()
    rate = models.DecimalField(max_digits=2, decimal_places=1)
