from django.shortcuts import render, HttpResponse

from .forms import PersonneForm
from Voiture.forms import VoitureForm



from .models import Personne


def personne_ajout(request):
    personnes = Personne.objects.all()
    print('bonjour')
    print(p.id_personne for p in personnes)
    # voiture = 
    context={
        "personne_form":PersonneForm(),
        "voiture_form":VoitureForm(),
        "personnes" : personnes
    }
    if request.method == "POST":
        data = PersonneForm(request.POST)        
        if data.is_valid():
            
            _nom = data.cleaned_data["nom"]
            _prenom = data.cleaned_data["prenom"]
            _genre = data.cleaned_data["genre"]
            
            Personne.objects.create(nom=_nom,prenom=_prenom,date_naissance=request.POST.get('dateinput'),genre=_genre)
            
            # print(nom,prenom,date_naissance,genre,)
            return HttpResponse("réussi")
        else:
            return HttpResponse(data)    
        
    
    return render(request, "inscriptionUtilisateur.html",context)

