from django.shortcuts import render, HttpResponse,redirect

from .forms import PersonneForm
from Voiture.forms import VoitureForm



from .models import Personne


def personne_ajout(request):
    personnes = Personne.objects.all()
    context={
        "personne_form":PersonneForm(),
        "personnes" : personnes
    }
    id_form = request.POST.get("id_Utilisateur")
    if request.method == "POST":
        data = PersonneForm(request.POST)        
        if data.is_valid():
            _nom = data.cleaned_data["nom"]
            _prenom = data.cleaned_data["prenom"]
            _genre = data.cleaned_data["genre"]
            _date_naissance = request.POST.get('dateinput')
            
            if id_form == "":
                personne = Personne.objects.create(nom=_nom,prenom=_prenom,date_naissance=_date_naissance,genre=_genre)
                personne.save()
            else:
                personne = Personne.objects.filter(id_personne=int(id_form)).first()
                personne.nom = _nom
                personne.prenom = _prenom
                personne.date_naissance = _date_naissance
                personne.genre = _genre
                personne.save()

            return redirect("home")
            return redirect("home")
        else:
            return HttpResponse("erreur")    
        
    
    return render(request, "inscriptionUtilisateur.html",context)

def personnes_supprimer(request, id):
    Personne.objects.filter(id_personne=id).first().delete()
    return redirect("home")
def personnes_modifier(request, id):
    personne = Personne.objects.filter(id_personne=id).first()
    
    context = {
        "title": "personnes",
        "idUtilisateur": personne.id_personne,
        "personne_form": PersonneForm(initial={'nom': personne.nom, 'prenom': personne.prenom,'date_naissance':personne.date_naissance,'genre':personne.genre}),
        "date_naissance":str(personne.date_naissance),
        "personnes": Personne.objects.all()
    }
    return render(request, "inscriptionUtilisateur.html", context)
    # return redirect("home")


