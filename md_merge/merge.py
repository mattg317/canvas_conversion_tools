from pathlib import Path
from read_json import get_titles
import re

def get_markdown():
    p = Path('Markdowns/.')
    mds = list(p.glob('*.md'))
    md_names = []

    for md in mds:
        md_names.append(md.name)
    md_names.sort()
    return md_names


output_file = "output_1.md"

def create_markdown(file_name, lesson_name):

    with open(file_name, 'w') as output_file:
        # TODO: Replace lesson name from JSON
        output_file.write(f"# {lesson_name} \n\n")

def write_markdown(file_name, md):

    with open(file_name, 'a') as output_file:
            md_file = "./Markdowns/" + md
            print(md_file)
            with open(md_file) as file:
                # TODO: replace DOGTEST with title from JSON
                output_file.write("## DOGTEST \n")
                for line in file:
                    output_file.write(line)

def merge_markdowns(output_file, md_names):
    start = ['1', '0']
    x = 1
    # JSON will be json[x][y][x]
    # x is module number
    # y is Text header sections
    # x is the page header. Note these start one above or equal third number
    # Start will take of of first two
    create_markdown(output_file, "Introduction to Module 1")

    for md in md_names:
        # Locate first two numbers in the markdown name
        file_numbers = re.findall("\d", md)
        print(f"file: {file_numbers}")

        # If numbers match the same section appened to out file
        if file_numbers[:2] == start:
            print(f"Match: {file_numbers[:3]}")
            print(f"writing: {md}")
            write_markdown(output_file, md)

        # When numbers change start a new output file
        else:
            start = file_numbers[:2]
            print("Start",start)
            x += 1
            output_file = f"output_{x}.md"
            create_markdown(output_file, "Introduction to Module 1")
            write_markdown(output_file, md)



j = 'JSONS/data.json'
lesson_name = get_titles(j, "1", "0")["0"]
create_markdown("output_1.md", lesson_name)