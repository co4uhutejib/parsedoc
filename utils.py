
def find_competence(data, competence):
    for prof,prof_record in data.items():
        for comp, comp_record in prof_record.items():
            if competence == comp:
                return comp_record
    return None
