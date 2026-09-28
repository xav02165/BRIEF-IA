
#========================================Calcul salaire chaque employés================================

#lie brief.py au fichier json
import json 
#lie fonction.py pour recuperer ma fonction
from fonction import salaire_mensuel 


     #Chargement du fichier JSON
with open('employes_data.json', 'r', encoding='utf-8') as fichier:
    donnees_entreprises = json.load(fichier)


# Deux boucles imbriqués
# Récupére le nom de l'entreprise et sa liste d'employés (items)
for entreprise, liste_employes in donnees_entreprises.items():
    print(f"\n--- Entreprise : {entreprise} ---")
    
    for employe in liste_employes:
        # liste les salariés et leur salaire
        salaire = salaire_mensuel(employe["contract_hours"], employe["weekly_hours_worked"], employe["hourly_rate"])
        
        print(f"Employé : {employe['name']} ({employe['job']}) -> Salaire : {salaire:} €")
   


#=============================Stat salariales: salaire moyen, +elevé, +bas de toutes les filiales======================
# Import des deux fonctions depuis fonction.py
from fonction import salaire_mensuel, afficher_stats_entreprise


salaires_techcorp = afficher_stats_entreprise("TechCorp", donnees_entreprises["TechCorp"])
salaires_DesignWorks = afficher_stats_entreprise("DesignWorks", donnees_entreprises["DesignWorks"])
salaires_ProjectLead = afficher_stats_entreprise("ProjectLead", donnees_entreprises["ProjectLead"])

    
#=============================Stat salariales: salaire moyen, +elevé, +bas de l'entreprise globale======================

# Calcul de la moyenne globale (somme de tous les salaires divisée par le nombre total d'employés)

salaires_entreprise_globale = (salaires_techcorp + salaires_DesignWorks + salaires_ProjectLead)


salaire_moyen_global = sum(salaires_entreprise_globale) / len(salaires_entreprise_globale)
salaire_moyen_global_arrondi = round(salaire_moyen_global, 2)

#Recherche du salaire minimum et maximum global parmi toutes les filiales
salaire_mini_global = min(salaires_entreprise_globale)
salaire_maxi_global = max(salaires_entreprise_globale)


print(f"Le salaire moyen au sein de l'entreprise est de : {salaire_moyen_global_arrondi} €")
print(f"Le salaire minimum global est de : {salaire_mini_global} €")
print(f"Le salaire maximum global est de : {salaire_maxi_global} €")
















