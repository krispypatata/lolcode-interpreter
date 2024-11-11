import sys
from lolcode_lexer import *

# For testing the implementation of the lexer
if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = lolcode_lex(characters)
    for token in tokens:
        print(token)

    # output to a file
    output_filename = "output.txt"
    with open(output_filename, 'w') as output_file:
        for token in tokens:
            output_file.write(str(token) + '\n')