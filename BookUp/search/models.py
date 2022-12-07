from django.db import models

# Create your models here.
import os

class Search(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.image.name
