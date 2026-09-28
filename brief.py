
#========================================Calcul salaire chaque employés================================

import json #lie brief.py au fichier json
from fonction import salaire_mensuel #lie fonction.py pour recuperer ma fonction


     #Chargement du fichier JSON
with open('employes_data.json', 'r', encoding='utf-8') as fichier:
    donnees_entreprises = json.load(fichier)

# Double boucle pour atteindre les employés
# .items() permet de récupérer le nom de l'entreprise et sa liste d'employés
for entreprise, liste_employes in donnees_entreprises.items():
    print(f"\n--- Entreprise : {entreprise} ---")
    
    for e in liste_employes:
        # liste les salariés et leur salaire
        salaire = salaire_mensuel(e["contract_hours"], e["weekly_hours_worked"], e["hourly_rate"])
        
        print(f"Employé : {e['name']} ({e['job']}) -> Salaire : {salaire:} €")
   


#=============================Stat salariales: salaire moyen, +elevé, +bas de toutes les filiales======================


#===Salaire moyen TechCorp===
# 1. Récupérer TechCorp
employes_techcorp = donnees_entreprises["TechCorp"]

salaires_techcorp = []

# 2. Calculer le salaire 
for donnee in employes_techcorp:
    salaire = salaire_mensuel(donnee["contract_hours"], donnee["weekly_hours_worked"], donnee["hourly_rate"])
    salaires_techcorp.append(salaire)

# 3. Calculer et afficher la moyenne
# (Somme de tous les salaires divisée par le nombre d'employés)
salaire_moyen_techcorp = sum(salaires_techcorp) / len(salaires_techcorp)
salaire_moyen_arrondi = round(salaire_moyen_techcorp, 2)

#===Salaire minimum et maximum TechCorp===
#1. Récuperer TechCorp
employes_techcorp = donnees_entreprises["TechCorp"]
salaire_mini_techcorp = []
salaire_maxi_techcorp = []

#Calcul salaire minimum
salaire_mini_techcorp = min(salaires_techcorp)
salaire_maxi_techcorp = max(salaires_techcorp)

print(f"Le salaire moyen au sein de TechCorp est de : {salaire_moyen_arrondi:} €")
print(f"le salaire minimum est de : {salaire_mini_techcorp} €")
print(f"le salaire maximum est de : {salaire_maxi_techcorp} €")


#===Salaire moyen DesignWorks===
# 1. Récuperer DesignWorks
employes_DesignWorks = donnees_entreprises["DesignWorks"]

salaires_DesignWorks = []

# 2. Calcul du salaire
for donneeB in employes_DesignWorks:
    salaire = salaire_mensuel(donneeB["contract_hours"], donneeB["weekly_hours_worked"], donneeB["hourly_rate"])
    salaires_DesignWorks.append(salaire)

# 3. Calculer et afficher la moyenne
# (Somme de tous les salaires divisée par le nombre d'employés)
salaire_moyen_DesignWorks = sum(salaires_DesignWorks) / len(salaires_DesignWorks)
salaire_moyen_arrondi = round(salaire_moyen_DesignWorks, 2)


#===Salaire minimum et maximum DesignWorks===
#1. Récuperer DesignWorks
employes_DesignWorks = donnees_entreprises["DesignWorks"]
salaire_mini_DesignWorks = []
salaire_maxi_DesignWorks = []

#Calcul salaire minimum
salaire_mini_DesignWorks = min(salaires_DesignWorks)
salaire_maxi_DesignWorks = max(salaires_DesignWorks)



print(f"Le salaire moyen au sein de DesignWorks est de : {salaire_moyen_arrondi:} €")
print(f"le salaire minimum est de : {salaire_mini_DesignWorks} €")
print(f"le salaire maximum est de : {salaire_maxi_DesignWorks} €")


    
#===Salaire moyen ProjectLead:===
# 1. Récuperer ProjectLead
employes_ProjectLead = donnees_entreprises["ProjectLead"]

salaires_ProjectLead = []

# 2. Calcul du salaire
for donneeC in employes_ProjectLead:
    salaire = salaire_mensuel(donneeC["contract_hours"], donneeC["weekly_hours_worked"], donneeC["hourly_rate"])
    salaires_ProjectLead.append(salaire)

# 3. Calculer et afficher la moyenne
# (Somme de tous les salaires divisée par le nombre d'employés)
salaire_moyen_ProjectLead = sum(salaires_ProjectLead) / len(salaires_ProjectLead)
salaire_moyen_arrondi = round(salaire_moyen_ProjectLead, 2)


#===Salaire minimum et maximum ProjectLead===
#1. Récuperer ProjectLead
employes_ProjectLead = donnees_entreprises["ProjectLead"]
salaire_mini_ProjectLead = []
salaire_maxi_ProjectLead = []

#Calcul salaire minimum
salaire_mini_ProjectLead = min(salaires_ProjectLead)
salaire_maxi_ProjectLead = max(salaires_ProjectLead)


print(f"Le salaire moyen au sein de ProjectLead est de : {salaire_moyen_arrondi:} €")
print(f"le salaire minimum est de : {salaire_mini_ProjectLead} €")
print(f"le salaire maximum est de : {salaire_maxi_ProjectLead} €")

    
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
















