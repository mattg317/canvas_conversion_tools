import fileinput
import re

def image_conversion(file_name):

    # Markdown regex pattern
    md_pattern = re.compile("(?<=\]\()media\/(.+)(?=\.png)")
    # md_pattern = re.compile("(?<=media\/)(.+)(?=\.png)")

    # HTML regex pattern
    html_pattern = re.compile("(?<=images\/module\_.\/)(.+)(?=\.png)")
    html_image_names = []

    # Loop through file html to pull the image name
    # Make sure each image tag in the HTML is on its on line
    html_file = "resources/html/" + file_name + ".html"
    for i, line in enumerate(open(html_file)):
        for match in re.finditer(html_pattern, line):
            print(f"Found on line {i + 1}: {match.group()}")
            html_image_names.append(match.group())
    print(html_image_names)

    print("Now Searching and Converting Markdown image links")
    md_file = "resources/md/" + file_name + ".md"

    for line in fileinput.input(md_file, inplace=1, backup='.bak'):
        match = md_pattern.search(line)
        if match:
            # Pull html image name from list
            new_image_name = html_image_names.pop(0)
            link_replace = "./assets/" + new_image_name
            line = re.sub(md_pattern, link_replace, line.rstrip())
        else:
            line = line.rstrip()
        print(line)