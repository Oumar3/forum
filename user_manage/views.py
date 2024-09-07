import pandas as pd 
import matplotlib.pyplot as plt
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import dbModel
# Create your views here.
def home(request):
    dbs = dbModel.objects.all()
    for db in dbs:
        df = pd.read_excel(db.db.path)
        # plt.plot(df)
        # plt.title(db.title)
        # plt.savefig(f'{db.title}.png')
        # plt.close()
    return render(request, 'user_manage/index.html',{'df': df})

# def read_db(request):
#     dbs = dbModel.objects.all()
   
#     return render(request, 'user_manage/read_db.html',{'dbs':dbs,})

@login_required
def hello_view(request):
    return render(request, 'user_manage/hello.html')

def login_view(request):
    error = False
    message = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            error = True
            message = "Utilisateur ou mot de passe invalide"
        else:
            user = authenticate(request, username=user.username,password=password)
            if user is not None:
                login(request, user)
                return redirect('user_manage:hello')
            else:
                error = True
                message = "Utilisateur ou mot de passe invalide"
            
    return render(request, 'user_manage/login.html',{'error': error, 'message': message})

def logout_view(request):
    return render(request, 'user_manage/logout.html')

def register_view(request):
    error = False
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmer = request.POST.get('confirmer')
        user = User.objects.filter(email=email)

        if user.exists():
            error = True
            message = "User already exists"
        if password != confirmer:
            error = True
            message = "le mot de passe ne correspond pas"
        if email == "" or password == "" or username == "":
            error = True
            message = "Veuillez remplir tous les champs"
        if error == False:
            user = User.objects.create_user(username, email, password)
            user.save()
            return render(request, 'user_manage/login.html')

    return render(request, 'user_manage/register.html', {'error': error, 'message': message})