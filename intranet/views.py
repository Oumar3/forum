from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Departement, Mesage
from .forms import MessageForm

@login_required
def liste_messages(request, departement_id):
    departement = get_object_or_404(Departement, id=departement_id)
    # Vérifie si l'utilisateur appartient au département
    if request.user.profile.departements.filter(id=departement.id).exists():
        messages = Mesage.objects.filter(departement=departement).order_by('-date_envoi')
        context = {
            'departement': departement,
            'messages': messages
        }
        return render(request, 'liste_messages.html', context)
    else:
        return render(request, 'access_denied.html')


@login_required
def envoyer_message(request, departement_id):
    departement = get_object_or_404(Departement, id=departement_id)

    if request.user.profile.departements.filter(id=departement.id).exists():
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.auteur = request.user
                message.departement = departement
                message.save()
                return redirect('liste_messages', departement_id=departement.id)
        else:
            form = MessageForm()
        
        context = {
            'departement': departement,
            'form': form
        }
        return render(request, 'messages/envoyer_message.html', context)
    else:
        return render(request, 'messages/access_denied.html')

@login_required
def repondre_message(request, message_id):
    message_original = get_object_or_404(Mesage, id=message_id)
    departement = message_original.departement

    if request.user.profile.departements.filter(id=departement.id).exists():
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                reponse = form.save(commit=False)
                reponse.auteur = request.user
                reponse.departement = departement
                reponse.save()
                return redirect('liste_messages', departement_id=departement.id)
        else:
            form = MessageForm()
        
        context = {
            'message_original': message_original,
            'form': form
        }
        return render(request, 'messages/repondre_message.html', context)
    else:
        return render(request, 'messages/access_denied.html')
