from django.db import models



class Player(models.Model):
    name    = models.CharField(max_length=50, unique=True, null=True)
    email   = models.EmailField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name
