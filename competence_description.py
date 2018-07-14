
# -*- coding: utf-8 -*-


def find_competence(data, competence):
    for prof,prof_record in data.items():
        for comp, comp_record in prof_record.items():
            if competence == comp:
                return comp_record
    return None

def print_competence_description(data, competence):
    comp_record = find_competence(data, competence)
    if None == comp_record:
        print('Competence "' + competence + '" not found')
        return

    print(u"Должен знать:")
    assert None != comp_record['should_know']
    print(comp_record['should_know'])

    print(u"Должен уметь:")
    assert None != comp_record['should_able']
    print(comp_record['should_able'])

    print(u"Должен владеть:")
    assert None != comp_record['should_master']
    print(comp_record['should_master'])