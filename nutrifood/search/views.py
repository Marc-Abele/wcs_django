from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")

def view_product(request, product_id):
    product=get_object_or_404(Product, id=product_id)
    try:
        context = {
            'product id': product_id,
            'product_name' : product.product_name,
            'food_groups' : product.food_groups,
            'nutriscore' : product.nutriscore,
            'allergens' : product.allergens,
            }
        return render(request, 'search/index.html', context)
    
    except Product.DoesNotExist:
        return HttpResponse("The product is not referenced", status=404)