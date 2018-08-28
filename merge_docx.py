
# -*- coding: utf-8 -*-

import sys
import argparse
from docx import Document

# TODO better?
# from https://stackoverflow.com/questions/24872527/combine-word-document-using-python-docx
def combine_word_documents(out_file, files):
    merged_document = Document()

    for index, file in enumerate(files):
        sub_doc = Document(file)

        # Don't add a page break if you've reached the last file.
        if index < len(files)-1:
           sub_doc.add_page_break()

        for element in sub_doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save(out_file)


parser = argparse.ArgumentParser(description='Merge few docx files into single file.')
parser.add_argument('OUTFILE', help='Output docx.')
parser.add_argument('INFILES', nargs='+', help='Input docx files')

args = parser.parse_args()

# print(args)

combine_word_documents(args.OUTFILE, args.INFILES)
