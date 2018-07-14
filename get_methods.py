
# -*- coding: utf-8 -*-

from utils import *

def print_get_methods(data, competences):
    competences = list(set(competences))

    methods = set()
    for competence in competences:
        comp_descr = find_competence(data, competence)
        assert None != comp_descr
        methods.add(comp_descr['methods'])

    for method in methods:
        print(method)