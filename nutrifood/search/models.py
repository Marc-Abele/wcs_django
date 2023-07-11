from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    product_name = models.CharField(max_length=255)
    food_groups = models.CharField(max_length=255)
    nutriscore = models.CharField(max_length=1)
    allergens = models.TextField()
    countries = models.CharField(max_length=255)
    keywords = models.TextField()
    ingredients_analysis_tags = models.TextField(default='')