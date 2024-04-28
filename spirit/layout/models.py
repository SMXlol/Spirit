from django.db import models


class Layout(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='layout/images')
    url = models.URLField(blank=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title


class Names(models.Model):
    name = models.CharField(max_length=200)
