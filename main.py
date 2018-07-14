
# -*- coding: utf-8 -*-

import sys
import argparse

from parse_table import prepare_data
from competence_description import print_competence_description
# from competence_description import print_competence_description
# from competence_description import print_competence_description

parser = argparse.ArgumentParser(description='Process doc table.')
parser.add_argument('doc', help='input file')
# parser.add_argument('first_cell', help='first cell in table')

subparsers = parser.add_subparsers(help='sub-command help')

#
parser_competence = subparsers.add_parser('competence',
    help='Print competence description: what should know, able and master.')
parser_competence.set_defaults(which='competence')
parser_competence.add_argument('NAME',
    help='Name of competence.')

#
parser_competence = subparsers.add_parser('discipline',
    help='FInd discipline if it exist.')
parser_competence.set_defaults(which='discipline')
parser_competence.add_argument('NAME',
    help='Discipline name.')

# 
parser_competence = subparsers.add_parser('methods',
    help='Print all from "Methods and technologies formation competence". Duplicate will be removed.')
parser_competence.set_defaults(which='methods')
parser_competence.add_argument('COMPETENCE', nargs='+',
    help='Discipline name.')



args = parser.parse_args()

data = prepare_data(args.doc, u"Вид профессиональной деятельности")
assert None != data

# print(args)

if args.which == 'competence':
    print_competence_description(data, args.NAME)

if args.which == 'discipline':
    # TODO
    print('find discipline: ' + args.NAME)

if args.which == 'methods':
    #TODO
    print('find methods: ' + args.COMPETENCE)