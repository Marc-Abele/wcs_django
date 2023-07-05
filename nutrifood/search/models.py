from django.db import models

class Product(models.Model):
    Ingredient = models.CharField(max_length=100)
