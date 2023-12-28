from django.db import models

# Create your models here.

class PostUserInfo(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    email = models.EmailField()
    xabar = models.TextField()

    def __str__(self):
        return f"{self.ism} {self.familiya}"
