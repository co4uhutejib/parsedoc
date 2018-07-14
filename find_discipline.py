
# -*- coding: utf-8 -*-

def get_discipline_list(data):
    disciplines = set()
    for prof,prof_record in data.items():
        for comp, comp_record in prof_record.items():
            for discipline in comp_record['disciplines']:
                disciplines.add(discipline.lower())
    return disciplines


def print_find_discipline(data, discipline):
    disciplines = get_discipline_list(data)
    if discipline.lower() in disciplines:
        print('Дисциплина: "' + discipline + '" найдена')
    else:
        print('Дисциплина: "' + discipline + '" ненайдена')