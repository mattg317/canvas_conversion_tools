from pathlib import Path
import PyInquirer


def list_files():
    # Create list of files in resources/html folder
    basepath = Path('resources/html/')
    files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())

    html_files = []
    for item in files_in_basepath:
        html_files.append(item.stem)

    print(html_files)


    # Create selection of which html file to convert
    questions = [
        {
            "type": 'list',
            'name': "html_file",
            'message': "What HTML file would you like to convert?",
            'choices':html_files,
        }
    ]

    answer = PyInquirer.prompt(questions)
    return answer["html_file"]
