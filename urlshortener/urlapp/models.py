from django.db import models
from .utils import create_shortcode

# Create your models here.

class Url(models.Model):
    url = models.URLField(max_length=254)
    shortcode = models.CharField(max_length=15)

    # def save(self, *args, **kwargs):
    #     self.shortcode =  create_shortcode(self)
    #     super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
