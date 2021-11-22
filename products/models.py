from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.TextField(default = 'Product')
    description = models.TextField(default = 'Some product')
    price       = models.TextField(default = '112358')
    summary     = models.TextField(default = 'Default!')
