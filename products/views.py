from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})

def add_products(request):
    """
    View function for adding a new product.

    This function handles both GET and POST requests. On a GET request, it
    renders the 'add_products.html' template with an empty form. On a POST
    request, it saves the form data and redirects to the 'index' page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """

    # Initialize an empty message
    message = ''
    form = ProductForm()
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = ProductForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Set the success message
            messages.success(request, "Le produit est ajouté avec succès !!")

            # Create a new empty form
            form = ProductForm()

            # Redirect to the 'index' page
            return  redirect('List_product:list_products')
        else:
            # Create a new empty form
            form = ProductForm()

    # Render the 'add_products.html' template with the form and message
    return render(request, 'add_products.html', {'form': form,})

def update_products(request, id):

    # Retrieve the product object from the database using the provided ID
    product = Product.objects.get(id=id)

    # Create a form instance with the product object as the data source
    form = ProductForm(instance=product)

    # Check if the request method is PUT
    if request.method == 'POST':
        # If the request method is PUT, create a form instance with the PUT data
        # and the product object as the data source
        form = ProductForm(request.POST, instance=product)

        # Check if the form data is valid
        if form.is_valid():
            # If the form data is valid, save the form data to the database
            form.save()

            # Redirect to the 'list_products' page
            return redirect('List_product:list_products')

    # Render the 'update_products.html' template with the form and product object
    return render(request, 'update_products.html', {'form': form, 'product': product})


def delete_products(request,id):
    product = Product.objects.get(id=id)
    if product:
        product.delete()
        return redirect('List_product:list_products')
    return redirect('list_products')



