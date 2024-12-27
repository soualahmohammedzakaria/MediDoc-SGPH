from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .data import medicaments_data


def home(request):
    return JsonResponse({"message": "Bienvenu sur l'API REST de gestion de la pharmacie hospitalière de MediDoc!"})

def medicaments(request):
    return JsonResponse(medicaments_data, safe=False)

@csrf_exempt
def verifier_ordonnance(request):
    if request.method != "POST":
        # Return 405 if the method is not POST
        return JsonResponse({
            "valide": False,
            "erreur": "Méthode non autorisée"
        }, status=405)

    try:
        # Parse the request body
        ordonnance = json.loads(request.body).get("ordonnance")
        if not ordonnance:
            # Return 400 if no ordonnance is provided
            return JsonResponse({
                "valide": False,
                "erreur": "L'ordonnance est manquante ou vide"
            }, status=400)

        # Iterate through each medication in the ordonnance
        for med in ordonnance:
            nom = med.get("nom")
            duree_prise = med.get("duree_prise")
            dose = med.get("dose")

            # Validate input structure
            if not nom or duree_prise is None or dose is None:
                return JsonResponse({
                    "valide": False,
                    "erreur": "Structure de l'ordonnance invalide"
                }, status=400)

            # Find the medicament in the database
            medicament = next((m for m in medicaments_data if m["nom"] == nom), None)

            if not medicament:
                # Medicament not found
                return JsonResponse({
                    "valide": False,
                    "erreur": f"Médicament {nom} inexistant"
                }, status=404)

            if duree_prise > medicament["max_duree_prise"]:
                # Duration exceeds the max allowed
                return JsonResponse({
                    "valide": False,
                    "erreur": f"La durée de prise du médicament {nom} dépasse la durée maximale"
                }, status=400)

            if dose > medicament["max_dose_jour"]:
                # Dose exceeds the max allowed
                return JsonResponse({
                    "valide": False,
                    "erreur": f"La dose de prise du médicament {nom} dépasse la dose maximale"
                }, status=400)

            if medicament["stock"] < 1:
                # Out of stock
                return JsonResponse({
                    "valide": False,
                    "erreur": f"Le médicament {nom} est en rupture de stock"
                }, status=400)

        # If all medications are valid
        return JsonResponse({
            "valide": True,
            "erreur": ""
        }, status=200)

    except json.JSONDecodeError:
        # Return 400 if JSON parsing fails
        return JsonResponse({
            "valide": False,
            "erreur": "Le corps de la requête doit être un JSON valide"
        }, status=400)