def output_console(text):
    """
    outputs data in the console
    """
    print(text)

def filewrite_python(filepath, text):
    """
    writes a file with python capabilities

    :return: text as arguments
    """
    with open(filepath, 'w') as file:
        file.write(text)

