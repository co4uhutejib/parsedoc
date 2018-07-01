import re

dump_test = False

def prepare_string(s):
    return s.strip()

def prepare_list(s, delim):
    return [x.strip() for x in list(filter(None, s.split(delim)))]

def prepare_comp_info(cells):
    result_data = dict()

    result_data["description"] = prepare_string(cells[2].text)
    result_data["significance"] = prepare_string(cells[3].text)

    result_data["should_know"] = prepare_string(cells[4].text)
    result_data["should_able"] = prepare_string(cells[5].text)
    result_data["should_master"] = prepare_string(cells[6].text)
    
    result_data["disciplines"] = prepare_list(cells[7].text, ',')
    result_data["methods"] = prepare_string(cells[8].text)

    return result_data


def prepare_data(path_to_doc, first_cell):
    print("---> Prepare data from: " + path_to_doc)
    from docx import Document

    document = Document(path_to_doc)

    #
    # print(type(args.first_cell))
    # print(args.first_cell)
    # print(":".join("{:04x}".format(ord(c)) for c in args.first_cell))
    # first_cell_utf8 = args.first_cell.encode('utf-8')
    # print(":".join("{:02x}".format(c) for c in first_cell_utf8))

    work_table = None

    # find table
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                str_val = str(cell.text)
                if str_val == first_cell:
                    work_table = table
            break

    if work_table is None:
        print("---> table not found")
        return None

    # print(work_table.rows[0].cells[0].text)

    result_data = dict()
    prof_record_name = None # this is 1 column
    prof_record = None # this is 1 column

    # skip first 3 rows
    rows_iter = iter(work_table.rows)
    for i in range(3):
        next(rows_iter)

    numb = 0
    for row in rows_iter:
        if dump_test:
            numb += 1
            if numb >= 3:
                break

        curr_prof_record_name = row.cells[0].text
        assert None != curr_prof_record_name
        if curr_prof_record_name != prof_record_name:
            prof_record_name = curr_prof_record_name
            assert not prof_record_name in result_data.keys()
            prof_record = dict()
            result_data[prof_record_name] = prof_record

        comptn_numb_name = row.cells[1].text
        # print(curr_prof_record_name)
        # for key in prof_record.keys():
        #     print(" - " + key)
        assert not comptn_numb_name in prof_record.keys()
        prof_record[comptn_numb_name] = prepare_comp_info(row.cells)

    if dump_test:
        print(result_data)

    return result_data