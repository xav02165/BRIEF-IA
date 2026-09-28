#===============Fonction principal=============

def salaire_mensuel(contract_hours, weekly_hours_worked, hourly_rate):
    # Des heures supplémentaires ont été effectuées
    if weekly_hours_worked > contract_hours:
        salaire_base_semaine = contract_hours * hourly_rate
        heures_sup_semaine = (weekly_hours_worked - contract_hours) * hourly_rate * 1.5
        salaire_mensuel_total = (salaire_base_semaine + heures_sup_semaine) * 4

    # Pas d'heures supplémentaires (heures normales ou moins)
    else:
        salaire_mensuel_total = (weekly_hours_worked * hourly_rate) * 4
        
    return salaire_mensuel_total



def afficher_stats_entreprise(nom_entreprise, liste_employes):
    salaires = []
    
    # Calcul du salaire de chaque employé 
    for e in liste_employes:
        s = salaire_mensuel(e["contract_hours"], e["weekly_hours_worked"], e["hourly_rate"])
        salaires.append(s)

    # Calculs des statistiques
    salaire_moyen_arrondi = round(sum(salaires) / len(salaires), 2)
    salaire_mini = min(salaires)
    salaire_maxi = max(salaires)

    # Affichage
    print(f"Le salaire moyen au sein de {nom_entreprise} est de : {salaire_moyen_arrondi} €")
    print(f"le salaire minimum est de : {salaire_mini} €")
    print(f"le salaire maximum est de : {salaire_maxi} €")

    
    return salaires