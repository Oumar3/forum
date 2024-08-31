from django.shortcuts import render

# Create your views here.
def apropos(request):
    return render(request, 'apropos.html')


def organigrame(request):
    return render(request, 'organigrame.html')