from django.db import models

class Register(models.Model):
    name = models.CharField('name', max_length=20)
    password1 = models.CharField('password', max_length=50)
    password2 = models.CharField('Confirm your password', max_length=50)

    def __str__(self):
        return self.name