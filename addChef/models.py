from django.db import models

# Create your models here.

class AddChef(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='chefs/')
    facebook = models.URLField(null = True, blank = True)
    twiter = models.URLField(null = True, blank = True)
    instagram = models.URLField(null = True, blank = True)

    def __str__(self):
        return self.name