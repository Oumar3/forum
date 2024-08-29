from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator
# Create your views here.
def list_products(request):
    products = Product.objects.all()
    
    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    # print(products)
    print(page_number)
    # print(page_obj)


    # return render(request, 'list_products.html', {'products': products})

    return render(request, 'list_products.html', {'products': products,'page_obj': page_obj})