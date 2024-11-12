from lexer import *

# read input file
data = "input.txt"
with open(data, 'r') as file:
    content = file.read()

# tokenize the content
tokens = tokenize(content)

# output to file
out = "output.txt"
with open(out, 'w') as file:
    for token, token_type in tokens:
        file.write(f'{token:<18}{token_type}\n')
