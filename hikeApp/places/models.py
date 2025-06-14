from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')
    description = models.CharField(max_length=100)
    trails = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name