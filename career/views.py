from django.shortcuts import render,redirect
from .models import Avis,Candidat
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.
def home(request):
    annonce = Avis.objects.all()
    return render(request, 'career/index.html', {'annonce': annonce})

# def avis_recurtement(request):
#     return render(request, 'career/liste_de_avis.html',{'annonce': annonce})

def detail(request,id):
    detail_avis = Avis.objects.get(id=id)
    return render(request,'career/detail.html',{'detail_avis':detail_avis})

@login_required
def postuler(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        cv = request.FILES.get('cv')
        lettre = request.FILES.get('lettre')
        experience_professionnelle = request.POST.get('experience_professionnelle')
        niveau_d_etude = request.POST.get('niveau_d_etude')
        specialite = request.POST.get('specialite')
        candidat = Candidat(nom=nom,prenom=prenom,email=email,telephone=telephone,cv=cv,lettre_de_motivation=lettre,experience_professionnelle=experience_professionnelle,niveau_d_etude=niveau_d_etude,specialite=specialite)
        candidat.save()
        return redirect('postuler')
    return render(request, 'career/postuler.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('career:postuler')
    return render(request, 'career/login.html')

def logout_user(request):
    logout(request)
    return redirect('career:career')
    

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
            return render(request, 'career/register.html')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('career:career')
    return render(request, 'career/register.html')