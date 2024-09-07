from django import forms
from .models import Mesage

class MessageForm(forms.ModelForm):
    class Meta:
        model = Mesage
        fields = ['departement', 'contenu']
