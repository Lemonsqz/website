from django.shortcuts import reverse

from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    img = models.TextField(max_length=500, blank=True)
    add_img = models.TextField(max_length=500, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })
