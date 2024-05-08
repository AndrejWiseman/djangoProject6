from django.db import models


# Create your models here.
class Blog(models.Model):
    naslov = models.CharField(max_length=120)
    sadrzaj = models.TextField()