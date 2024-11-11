import lexer

RESERVED = 'Reserved'

# Literals
NUMBR = 'Integer'
NUMBAR = 'Float'
TROOF = 'Boolean'
YARN = 'String'
IDENTIFIER = 'Identifier'
TYPE = 'TYPE'

token_exprs = [
    (r'[ \n\t]+',                     None),   # whitespace
    (r'BTW[^\n]*',                    None),   # single line comments
    (r'OBTW\s*((.|\n)*?)\s*TLDR',     None),   # multi-line comments # multiline comments
    (r'HAI',                      RESERVED),
    (r'KTHXBYE',                  RESERVED),
    (r'WAZZUP',                   RESERVED),
    (r'BUHBYE',                   RESERVED),
    (r'I HAS A[ \t]+',            RESERVED),
    (r'ITZ[ \t]+',                RESERVED),
    (r'R[ \t]+',                  RESERVED),
    (r'SUM OF[ \t]+',             RESERVED),
    (r'DIFF OF[ \t]+',            RESERVED),
    (r'PRODUKT OF[ \t]+',         RESERVED),
    (r'QUOSHUNT OF[ \t]+',        RESERVED),
    (r'MOD OF[ \t]+',             RESERVED),
    (r'BIGGR OF[ \t]+',           RESERVED),
    (r'SMALLR OF[ \t]+',          RESERVED),
    (r'BOTH OF[ \t]+',            RESERVED),
    (r'EITHER OF[ \t]+',          RESERVED),
    (r'WON OF[ \t]+',             RESERVED),
    (r'NOT[ \t]+',                RESERVED),
    (r'ANY OF[ \t]+',             RESERVED),
    (r'ALL OF[ \t]+',             RESERVED),
    (r'AN YR[ \t]+',              RESERVED),
    (r'AN[ \t]+',                 RESERVED),
    (r'BOTH SAEM[ \t]+',          RESERVED),
    (r'DIFFRINT[ \t]+',           RESERVED),
    (r'SMOOSH[ \t]+',             RESERVED),
    (r'MAEK[ \t]+',               RESERVED),
    (r'A[ \t]+',                  RESERVED),
    (r'IS NOW A[ \t]+',           RESERVED),
    (r'VISIBLE[ \t]+',            RESERVED),
    (r'GIMMEH[ \t]+',             RESERVED),
    (r'O RLY\?',                  RESERVED),
    (r'YA RLY',                   RESERVED),
    (r'MEBBE[ \t]+',              RESERVED),
    (r'NOWAI',                    RESERVED),
    (r'OIC',                      RESERVED),
    (r'WTF\?',                    RESERVED),
    (r'OMG[ \t]+',                RESERVED),
    (r'OMGWTF',                   RESERVED),
    (r'IM IN YR[ \t]+',           RESERVED),
    (r'UPPIN[ \t]+',              RESERVED),
    (r'NERFIN[ \t]+',             RESERVED),
    (r'YR[ \t]+',                 RESERVED),
    (r'TIL[ \t]+',                RESERVED),
    (r'WILE[ \t]+',               RESERVED),
    (r'IM OUTTA YR[ \t]+',        RESERVED),
    (r'HOW IZ I[ \t]+',           RESERVED),
    (r'IF U SAY SO',              RESERVED),
    (r'GTFO',                     RESERVED),
    (r'FOUND YR[ \t]+',           RESERVED),
    (r'I IZ[ \t]+',               RESERVED),
    (r'MKAY[ \t]+',               RESERVED),
    (r'-?[0-9]+\.[0-9]+',           NUMBAR),     # Float
    (r'-?[0-9]+',                    NUMBR),     # Integer
    (r'"[^"]*"',                      YARN),     # String
    (r'WIN|FAIL',                    TROOF),     # Boolean
    (r'NOOB|NUMBR|NUMBAR|YARN|TROOF', TYPE),     # Type
    (r'[a-zA-Z][a-zA-Z0-9_]*',  IDENTIFIER),     # Identifier
]

def lolcode_lex(characters):
    return lexer.lex(characters, token_exprs)
