#! /bin/bash

# python3 main.py in_doc.docx competence "ОК-6"

# python3 main.py in_doc.docx discipline "Правоведение"
# python3 main.py in_doc.docx discipline "asdasdПравоведение"

# python3 main.py in_doc.docx methods "ОК-6" "ОК-4" "ОК-7" "ОК-8" "ПК-8"

python3 merge_docx.py out.docx in1.docx in2.docx


# python3 main.py in_doc.docx "$@"
