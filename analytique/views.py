from django.shortcuts import render
from products.models import Product
import json
# Create your views here.
def home(request):
    products = Product.objects.all()
    labels = [product.name for product in products]
    data = [float(product.price) for product in products]
    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }
    return render(request,'analytique/home.html',context)

def area_chart(request):
    return render(request,'analytique/area_chart.html')

def datatable(request):
    return render(request,'analytique/datatable.html')
