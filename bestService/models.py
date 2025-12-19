from django.db import models

# Create your models here.

class BestService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='best_services/')
    learn_more_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name