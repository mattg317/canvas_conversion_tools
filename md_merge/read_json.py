import json


j = open('JSONS/data.json')

def get_titles(json_file, module_no, section_no):
    j = open(json_file)

    data = json.load(j)

    j.close()
    return data[module_no][section_no]

j = 'JSONS/data.json'
print(get_titles(j, "1", "0"))
