from django.db import models

# Create your models here.
class ApiData(models.Model):
    name=models.CharField(max_length=100)
    classname=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(max_length=300)
    phonenumber=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name