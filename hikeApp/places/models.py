from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name