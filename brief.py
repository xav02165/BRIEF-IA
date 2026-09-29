
# ========================================Calcul salaire chaque employés================================
import csv
import json 
from fonction import salaire_mensuel, afficher_stats_entreprise 


# Chargement du fichier JSON
with open('employes_data.json', 'r', encoding='utf-8') as fichier:
    donnees_entreprises = json.load(fichier)

# Ouverture et Création du fichier CSV des employés
with open('employes_resultats.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
    ecripteur = csv.writer(fichier_csv)
    
    # Colonnes
    ecripteur.writerow(["Entreprise", "Nom", "Poste", "Salaire (€)"])

    # Double boucle
    for entreprise, liste_employes in donnees_entreprises.items():
        print(f"\n--- Entreprise : {entreprise} ---")
        
        for employe in liste_employes:
            # Calcul du salaire
            salaire = salaire_mensuel(employe["contract_hours"], employe["weekly_hours_worked"], employe["hourly_rate"])

            # Écriture de la ligne dans le CSV
            ecripteur.writerow([entreprise, employe["name"], employe["job"], salaire])
            
            # Affichage 
            print(f"Employé : {employe['name']} ({employe['job']}) -> Salaire : {salaire} €")


# =============================Stat salariales par filiale======================

salaires_techcorp = afficher_stats_entreprise("TechCorp", donnees_entreprises["TechCorp"])
salaires_DesignWorks = afficher_stats_entreprise("DesignWorks", donnees_entreprises["DesignWorks"])
salaires_ProjectLead = afficher_stats_entreprise("ProjectLead", donnees_entreprises["ProjectLead"])

    
# =============================Stat salariales globales======================

salaires_entreprise_globale = (salaires_techcorp + salaires_DesignWorks + salaires_ProjectLead)

salaire_moyen_global = sum(salaires_entreprise_globale) / len(salaires_entreprise_globale)
salaire_moyen_global_arrondi = round(salaire_moyen_global, 2)

salaire_mini_global = min(salaires_entreprise_globale)
salaire_maxi_global = max(salaires_entreprise_globale)

print(f"\nLe salaire moyen au sein de l'entreprise est de : {salaire_moyen_global_arrondi} €")
print(f"Le salaire minimum global est de : {salaire_mini_global} €")
print(f"Le salaire maximum global est de : {salaire_maxi_global} €")


# =============================Export CSV des statistiques======================

# Calculs des statistiques par filiale
moyen_techcorp = round(sum(salaires_techcorp) / len(salaires_techcorp), 2)
mini_techcorp = min(salaires_techcorp)
maxi_techcorp = max(salaires_techcorp)

moyen_designworks = round(sum(salaires_DesignWorks) / len(salaires_DesignWorks), 2)
mini_designworks = min(salaires_DesignWorks)
maxi_designworks = max(salaires_DesignWorks)

moyen_projectlead = round(sum(salaires_ProjectLead) / len(salaires_ProjectLead), 2)
mini_projectlead = min(salaires_ProjectLead)
maxi_projectlead = max(salaires_ProjectLead)

# Écriture du fichier 
with open('statistiques.csv', 'w', newline='', encoding='utf-8') as fichier_stats_csv:
    ecripteur_stats = csv.writer(fichier_stats_csv)
    
    # Tableau CSV
    ecripteur_stats.writerow(["Entité", "Salaire Moyen (€)", "Salaire Minimum (€)", "Salaire Maximum (€)"])
    
    # Écriture des lignes de chaque filiale
    ecripteur_stats.writerow(["TechCorp", moyen_techcorp, mini_techcorp, maxi_techcorp])
    ecripteur_stats.writerow(["DesignWorks", moyen_designworks, mini_designworks, maxi_designworks])
    ecripteur_stats.writerow(["ProjectLead", moyen_projectlead, mini_projectlead, maxi_projectlead])
    
    # Écriture de la ligne globale
    ecripteur_stats.writerow(["Entreprise Globale", salaire_moyen_global_arrondi, salaire_mini_global, salaire_maxi_global])

print("\nLe fichier 'statistiques.csv' a été créé")













