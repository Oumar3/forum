from django.urls import path
app_name = "intranet"
from . import views

urlpatterns = [
    path('liste_messages/<int:departement_id>', views.liste_messages, name="liste_messages"),
    path('envoyer_message/<int:departement_id>', views.envoyer_message, name="envoyer_message"),
    path('repondre_message/<int:message_id>', views.repondre_message, name="repondre_message"),
]