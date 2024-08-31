from django.shortcuts import render
from .models import Avis,Candidat

# Create your views here.
def home(request):
    annonce = Avis.objects.all()
    return render(request, 'career/index.html', {'annonce': annonce})

# def avis_recurtement(request):
#     return render(request, 'career/liste_de_avis.html',{'annonce': annonce})