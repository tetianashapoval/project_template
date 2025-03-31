def input_console():
    """
    makes the user input data from the console
    """
    return input("enter something:")

def fileread_python(filepath):
    """
    reads the file using python capabilities

    :return: content of the file as a string
    """
    with open(filepath, 'r') as file:
        return file.read()

def fileread_pandas(filepath):
    """
    reads the file using pandas

    :return: content of the file as a dataframe
    """
    import pandas as pd
    data = pd.read_csv(filepath)
    return data

