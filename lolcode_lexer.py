import lexer

# RESERVED = 'Reserved' # inital constant tag for KEYWORDS

token_exprs = [
    (r'[ \n\t]+',                     None),   # whitespace (ignore)
    (r'BTW[^\n]*',                    None),   # single line comments (ignore)
    (r'OBTW\s*((.|\n)*?)\s*TLDR',     None),   # multi-line comments (ignore)
    (r'HAI',                          'Program Start Delimeter'),
    (r'KTHXBYE',                      'Program End Delimeter'),
    (r'WAZZUP',                       'Variable Declaration Start Delimeter'),
    (r'BUHBYE',                       'Variable Declaration End Delimeter'),
    (r'I HAS A[ \t]+',                'Variable Declaration'),
    (r'ITZ[ \t]+',                    'Variable Initialization'),
    (r'R[ \t]+',                      'Assignment Keyword'),
    (r'SUM OF[ \t]+',                 'Addition Operator'),
    (r'DIFF OF[ \t]+',                'Subtraction Operator'),
    (r'PRODUKT OF[ \t]+',             'Multiplication Operator'),
    (r'QUOSHUNT OF[ \t]+',            'Division Operator'),
    (r'MOD OF[ \t]+',                 'Modulus Operator'),
    (r'BIGGR OF[ \t]+',               'Greater Than Operator'),
    (r'SMALLR OF[ \t]+',              'Less Than Operator'),
    (r'BOTH OF[ \t]+',                'AND Operator'),
    (r'EITHER OF[ \t]+',              'OR Operator'),
    (r'WON OF[ \t]+',                 'XOR Operator'),
    (r'NOT[ \t]+',                    'NOT Operator'),
    (r'ANY OF[ \t]+',                 'ANY Operator'),
    (r'ALL OF[ \t]+',                 'ALL Operator'),
    (r'AN YR[ \t]+',                  'Additional Parameter Variable'),
    (r'AN[ \t]+',                     'Operand Connector'),
    (r'BOTH SAEM[ \t]+',              'Equality Operator'),
    (r'DIFFRINT[ \t]+',               'Inequality Operator'),
    (r'SMOOSH[ \t]+',                 'String Concatenate Operator'),
    (r'MAEK[ \t]+',                   'Typecast MAEK Operator'),
    (r'A[ \t]+',                      'Typecast Specifier'),
    (r'IS NOW A[ \t]+',               'Typecast IS NOW A Operator'),
    (r'VISIBLE[ \t]+',                'Print Statement'),
    (r'GIMMEH[ \t]+',                 'Input Statement'),
    (r'O RLY\?',                      'Conditional Start Delimeter'),
    (r'YA RLY',                       'If Clause'),
    (r'MEBBE[ \t]+',                  'Else-If Clause'),
    (r'NO WAI',                       'Else Clause'),
    (r'OIC',                          'Conditional End Delimeter'),
    (r'WTF\?',                        'Switch-Case Start Delimeter'),
    (r'OMG[ \t]+',                    'Case Clause'),
    (r'OMGWTF',                       'Switch-Case End Delimeter'),
    (r'IM IN YR[ \t]+',               'Loop Start Delimeter'),
    (r'UPPIN[ \t]+',                  'Increment Operator'),
    (r'NERFIN[ \t]+',                 'Decrement Operator'),
    (r'YR[ \t]+',                     'Parameter Variable'),
    (r'TIL[ \t]+',                    'Until Loop'),
    (r'WILE[ \t]+',                   'While Loop'),
    (r'IM OUTTA YR[ \t]+',            'Loop End Delimeter'),
    (r'HOW IZ I[ \t]+',               'Function Start Delimeter'),
    (r'IF U SAY SO',                  'Function End Delimeter'),
    (r'GTFO',                         'Function Return'),
    (r'FOUND YR[ \t]+',               'Function Return Value'),
    (r'I IZ[ \t]+',                   'Function Call'),
    (r'MKAY',                         'Statement End Delimeter'),
    (r'-?[0-9]+\.[0-9]+',             'Float'),         # Float
    (r'-?[0-9]+',                     'Integer'),       # Integer
    (r'"[^"]*"',                      'String'),        # String
    (r'WIN|FAIL',                     'Boolean'),       # Boolean
    (r'NOOB|NUMBR|NUMBAR|YARN|TROOF', 'Literal Type'),  # Type
    (r'[a-zA-Z][a-zA-Z0-9_]*',        'Identifier'),    # Identifier
]

def lolcode_lex(characters):
    return lexer.lex(characters, token_exprs)
