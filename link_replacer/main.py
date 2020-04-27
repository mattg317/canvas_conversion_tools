from list_files import list_files
from image_replace import image_conversion

"""Converts markdown images to the correct image name located in the html file
This scripts assumes all html files are located in resources/html/ and all md
are located in resources/md/

Both the HTML and MD files should have the same file name.
"""

def main():
    file_convert = list_files()
    image_conversion(file_convert)
    print("Markdown links converted")

if __name__ == '__main__':
    main()