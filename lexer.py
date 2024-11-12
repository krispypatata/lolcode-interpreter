import re

# regex patterns and their corresponding classification
token_patterns = {
    # program keywords, comments, variables
    r'HAI': 'Program Start Delimiter',
    r'KTHXBYE': 'Program End Delimiter',
    r'WAZZUP': 'Variable Declaration Start Delimiter',
    r'BUHBYE': 'Variable Declaration End Delimiter',
    r'BTW[ \t]+': 'Inline Comment Start',
    r'OBTW[ \t]+': 'Multiline Comment Start',
    r'TLDR[ \t]+': 'Multiline Comment End',
    r'I HAS A[ \t]+': 'Variable Declaration',
    r'ITZ[ \t]+': 'Variable Initialization',
    r'R[ \t]+': 'Assignment Keyword',

    # operations
    r'SUM OF[ \t]+': 'Arithmetic Operator',
    r'DIFF OF[ \t]+': 'Arithmetic Operator',
    r'PRODUKT OF[ \t]+': 'Arithmetic Operator',
    r'QUOSHUNT OF[ \t]+': 'Arithmetic Operator',
    r'MOD OF[ \t]+': 'Arithmetic Operator',
    r'BIGGR OF[ \t]+': 'Relational Operator',
    r'SMALLR OF[ \t]+': 'Relational Operator',
    r'BOTH OF[ \t]+': 'Boolean Operator',
    r'EITHER OF[ \t]+': 'Boolean Operator',
    r'WON OF[ \t]+': 'Boolean Operator',
    r'NOT[ \t]+': 'Boolean Operator',
    r'ANY OF[ \t]+': 'Boolean Operator',
    r'ALL OF[ \t]+': 'Boolean Operator',
    r'BOTH SAEM[ \t]+': 'Comparison Operator',
    r'DIFFRINT[ \t]+': 'Comparison Operator',
    r'SMOOSH[ \t]+': 'String Concatenate Operator',
    r'MAEK[ \t]+': 'Typecast Operator',
    r'A[ \t]+': 'Typecast Operator',
    r'IS NOW A[ \t]+': 'Typecast Operator',

    # statements
    r'VISIBLE[ \t]+': 'Print Statement',
    r'GIMMEH[ \t]+': 'Input Statement',
    r'O RLY\?': 'Conditional Start Delimiter',
    r'YA RLY': 'If Clause',
    r'MEBBE[ \t]+': 'Else If Clause',
    r'NO WAI': 'Else Clause',
    r'OIC': 'Conditional End Delimiter',
    r'WTF\?': 'Switch-Case Start Delimiter',
    r'OMG[ \t]+': 'Case Clause',
    r'OMGWTF': 'Switch-Case End Delimiter',
    r'IM IN YR[ \t]+': 'Loop Start Delimiter',
    r'UPPIN[ \t]+': 'Loop Operation',
    r'NEFFIN[ \t]+': 'Loop Operation',
    r'AN YR[ \t]+': 'Loop Parameter Variable',
    r'AN[ \t]+': 'Loop Parameter Variable',
    r'YR[ \t]+': 'Loop Parameter Variable',
    r'TIL[ \t]+': 'Loop Condition',
    r'WILE[ \t]+': 'Loop Condition',
    r'IM OUTTA YR[ \t]+': 'Loop End Delimiter',

    # functions
    r'HOW IZ I[ \t]+': 'Function Start Delimiter',
    r'IF U SAY SO': 'Function End Delimiter',
    r'GTFO': 'Function Return',
    r'FOUND YR[ \t]+': 'Function Return',
    r'I IZ[ \t]+': 'Function Call',
    r'MKAY[ \t]+': 'Statement End Delimiter',

    # literals
    r'-?[0-9]+\.[0-9]+': 'NUMBAR Literal',  # float
    r'-?[0-9]+': 'NUMBR Literal',           # integer
    #r'\'[^\']*\'': 'YARN Literal',          # string
    r'\".*\"': 'YARN Literal',              # string
    r'WIN|FAIL': 'TROOF Literal',           # boolean
    r'NOOB|NUMBR|NUMBAR|YARN|TROOF': 'TYPE Literal',

    # identifiers
    r'[a-zA-Z][a-zA-Z0-9_]*': 'Identifier'
}

def tokenize(text):
    tokens = []
    position = 0

    while position < len(text):
        match = False

        # skip inline and multiline comments
        if re.match(r'BTW[ \t]+', text[position:]):
            newline_pos = text.find('\n', position)
            if newline_pos != -1:
                position = newline_pos+1
            else:
                position = len(text)
            continue

        if re.match(r'OBTW[ \t]+', text[position:]):
            end_pos = text.find('TLDR', position)
            if end_pos != -1:
                position = end_pos+len('TLDR')
            else:
                position = len(text)
            continue

        # tokenize text using predefined patterns
        for pattern, token_type in token_patterns.items():
            regex = re.compile(pattern)
            match = regex.match(text, position)
            if match:
                token = match.group(0)
                tokens.append((token, token_type))
                position = match.end()
                match = True
                break

        if not match:
            position += 1

    return tokens