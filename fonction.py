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
