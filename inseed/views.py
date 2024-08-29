from django.shortcuts import render

# Create your views here.
def inseed(request):
    return render(request, 'inseed.html')