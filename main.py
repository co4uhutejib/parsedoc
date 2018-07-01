
# -*- coding: utf-8 -*-

import sys
import argparse

from parse_table import prepare_data

parser = argparse.ArgumentParser(description='process doc table.')
parser.add_argument('doc', help='input file')
# parser.add_argument('first_cell', help='first cell in table')

args = parser.parse_args()

data = prepare_data(args.doc, u"Вид профессиональной деятельности")
assert data != None


