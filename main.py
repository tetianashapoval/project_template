from app.io.input import input_console, fileread_python, fileread_pandas
from app.io.output import output_console, filewrite_python

def main():
    my_input = input_console()
    output_console(my_input)
    filewrite_python('output.txt', my_input)

    file_data = fileread_python('input.txt')
    output_console(file_data)
    filewrite_python('output.txt', file_data)

    pandas = fileread_pandas('input.csv')
    output_console(pandas)
    filewrite_python('output.txt', str(pandas))


if __name__ == '__main__':
    main()




