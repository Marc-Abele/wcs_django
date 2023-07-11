from django.core.management.base import BaseCommand, CommandError
from search.models import Product 
import requests
import json

class Command(BaseCommand):
    help = 'Retrieves product listings by category'
    
    def add_arguments(self, parser):
        parser.add_argument('category', nargs = '+', type = str)
        
    def handle(self, *args, **kwargs):
        category = str(kwargs['category'])
        url = 'https://world.openfoodfacts.org/category/'+category+'/?page_size=100.json'
        r = requests.get(url)
        products = json.loads(r.text)['products']
        for product in products:
            try:
                new_prod = Product(
                    id = product.get('_id'),
                    product_name = product.get('product_name', ''),
                    food_groups = product.get('food_groups', ''),
                    nutriscore = product.get('nutriscore_grade', ''),
                    allergens = product.get('allergens', ''),
                    countries = product.get('countries', ''),
                    keywords = product.get('_keywords', ''),
                    ingredients_analysis_tags=product.get('ingredients_analysis_tags', ''),
                )
                new_prod.save()
            except Exception as e:
                print("An error occured, check your category please", str(e))