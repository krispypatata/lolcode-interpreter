import lexer

# RESERVED = 'Reserved' # inital constant tag for KEYWORDS

# Proram keywords, variables
HAI = 'Program Start Delimeter'
KTHXBYE = 'Program End Delimeter'
WAZZUP = 'Variable Declaration Start Delimeter'
BUHBYE = 'Variable Declaration End Delimeter'
I_HAS_A ='Variable Declaration'
ITZ = 'Variable Initialization'
R = 'Assignment Keyword'

# Operations
SUM_OF = 'Arithmetic Operator'
DIFF_OF = 'Arithmetic Operator'
PRODUKT_OF = 'Arithmetic Operator'
QUOSHUNT_OF = 'Arithmetic Operator'
MOD_OF = 'Arithmetic Operator'
BIGGR_OF = 'Relational Operator'
SMALLR_OF = 'Relational Operator'
BOTH_OF = 'Boolean Operator'
EITHER_OF = 'Boolean Operator'
WON_OF = 'Boolean Operator'
NOT = 'Boolean Operator'
ANY_OF = 'Boolean Operator'
ALL_OF = 'Boolean Operator'
BOTH_SAEM = 'Comparison Operator'
DIFFRINT = 'Comparison Operator'
SMOOSH = 'String Concatenate Operator'
MAEK = 'Typecast Operator'
A = 'Typecast Operator'
IS_NOW_A = 'Typecast Operator'

# Part of the expression for operands
AN = 'Operand Connector'
YR = 'Parameter Variable'
AN_YR = 'Additional Parameter Variable'

# Statements
VISIBLE = 'Print Statement'
GIMMEH = 'Input Statement'
O_RLY = 'Conditional Start Delimeter'
YA_RLY = 'If Clause'
MEBBE = 'Else If Clause'
NO_WAI = 'Else Clause'
OIC = 'Conditional End Delimeter'
WTF = 'Switch-Case Start Delimeter'
OMG = 'Case Clause'
OMGWTF = 'Switch-Case End Delimeter'
IM_IN_YR = 'Loop Start Delimeter'
UPPIN = 'Loop Operation'
NERFIN = 'Loop Operation'
TIL = 'Loop Condition'
WILE = 'Loop Condition'
IM_OUTTA_YR = 'Loop End Delimeter'

# Functions
HOW_IZ_I = 'Function Start Delimeter'
IF_U_SAY_SO = 'Function End Delimeter'
GTFO = 'Function Return'
FOUND_YR = 'Function Return'
I_IZ = 'Function Call'
MKAY = 'Statement End Delimeter'

# Literals
NUMBR = 'Integer'
NUMBAR = 'Float'
TROOF = 'Boolean'
YARN = 'String'
TYPE = 'Literal Type'

# Identifier
IDENTIFIER = 'Identifier'

token_exprs = [
    (r'[ \n\t]+',                     None),   # whitespace (ignore)
    (r'BTW[^\n]*',                    None),   # single line comments (ignore)
    (r'OBTW\s*((.|\n)*?)\s*TLDR',     None),   # multi-line comments (ignore)
    (r'HAI',                           HAI),
    (r'KTHXBYE',                   KTHXBYE),
    (r'WAZZUP',                     WAZZUP),
    (r'BUHBYE',                     BUHBYE),
    (r'I HAS A[ \t]+',             I_HAS_A),
    (r'ITZ[ \t]+',                     ITZ),
    (r'R[ \t]+',                         R),
    (r'SUM OF[ \t]+',               SUM_OF),
    (r'DIFF OF[ \t]+',             DIFF_OF),
    (r'PRODUKT OF[ \t]+',       PRODUKT_OF),
    (r'QUOSHUNT OF[ \t]+',     QUOSHUNT_OF),
    (r'MOD OF[ \t]+',               MOD_OF),
    (r'BIGGR OF[ \t]+',           BIGGR_OF),
    (r'SMALLR OF[ \t]+',         SMALLR_OF),
    (r'BOTH OF[ \t]+',             BOTH_OF),
    (r'EITHER OF[ \t]+',         EITHER_OF),
    (r'WON OF[ \t]+',               WON_OF),
    (r'NOT[ \t]+',                     NOT),
    (r'ANY OF[ \t]+',               ANY_OF),
    (r'ALL OF[ \t]+',               ALL_OF),
    (r'AN YR[ \t]+',                 AN_YR),
    (r'AN[ \t]+',                       AN),
    (r'BOTH SAEM[ \t]+',         BOTH_SAEM),
    (r'DIFFRINT[ \t]+',           DIFFRINT),
    (r'SMOOSH[ \t]+',               SMOOSH),
    (r'MAEK[ \t]+',                   MAEK),
    (r'A[ \t]+',                         A),
    (r'IS NOW A[ \t]+',           IS_NOW_A),
    (r'VISIBLE[ \t]+',             VISIBLE),
    (r'GIMMEH[ \t]+',               GIMMEH),
    (r'O RLY\?',                     O_RLY),
    (r'YA RLY',                     YA_RLY),
    (r'MEBBE[ \t]+',                 MEBBE),
    (r'NO WAI',                      NO_WAI),
    (r'OIC',                           OIC),
    (r'WTF\?',                         WTF),
    (r'OMG[ \t]+',                     OMG),
    (r'OMGWTF',                     OMGWTF),
    (r'IM IN YR[ \t]+',           IM_IN_YR),
    (r'UPPIN[ \t]+',                 UPPIN),
    (r'NERFIN[ \t]+',               NERFIN),
    (r'YR[ \t]+',                       YR),
    (r'TIL[ \t]+',                     TIL),
    (r'WILE[ \t]+',                   WILE),
    (r'IM OUTTA YR[ \t]+',     IM_OUTTA_YR),
    (r'HOW IZ I[ \t]+',           HOW_IZ_I),
    (r'IF U SAY SO',           IF_U_SAY_SO),
    (r'GTFO',                         GTFO),
    (r'FOUND YR[ \t]+',           FOUND_YR),
    (r'I IZ[ \t]+',                   I_IZ),
    (r'MKAY',                         MKAY),
    (r'-?[0-9]+\.[0-9]+',           NUMBAR),     # Float
    (r'-?[0-9]+',                    NUMBR),     # Integer
    (r'"[^"]*"',                      YARN),     # String
    (r'WIN|FAIL',                    TROOF),     # Boolean
    (r'NOOB|NUMBR|NUMBAR|YARN|TROOF', TYPE),     # Type
    (r'[a-zA-Z][a-zA-Z0-9_]*',  IDENTIFIER),     # Identifier
]

def lolcode_lex(characters):
    return lexer.lex(characters, token_exprs)
