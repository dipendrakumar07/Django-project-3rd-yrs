from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, default="About Our Traditional Ice Creams Since 1950")
    description = models.TextField()
    founder_name = models.CharField(max_length=100, default="Founder Unknown")
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title
