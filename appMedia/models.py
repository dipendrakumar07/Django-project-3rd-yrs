from django.db import models

class Icecreams(models.Model):
    icecream_flavours = models.CharField(max_length=250)
    icecream_price = models.CharField(max_length=250)
    icecream_img = models.FileField(upload_to="icecream", max_length=250, null=True, default=None)

    def _str_(self):
        return self.icecream_flavours