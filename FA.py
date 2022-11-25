import sys
import re

# list token untuk syntax ke token
token_exp = [
    (r'[ \t]+',                 None),
    (r'//[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # Integer dan String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    
    # Delimiter
    (r'\(',                     "KBKI"), # Kurung Biasa Kiri
    (r'\)',                     "KBKA"), # Kurung Biasa Kanan
    (r'\[',                     "KSKI"), # Kurung Siku Kiri
    (r'\]',                     "KSKA"), # Kurung Siku Kanan
    (r'\{',                     "KKKI"), # Kurung Kurawal Kiri
    (r'\}',                     "KKKA"), # Kurung Kurawal Kanan
    (r'\;',                     "TITIKOMA"),
    (r'\:',                     "TITIKDUA"),
    (r'\n',                     "NEWLINE"),

    # Operator
    (r'\*\*',                   "POW"),
    (r'!',                      "NOT"),
    (r'<=',                     "LEQ"),
    (r'<',                      "L"),
    (r'>=',                     "GEQ"),
    (r'>',                      "G"),
    (r'!=',                     "NEQ"),
    (r'\==',                    "ISEQ"),
    (r'\=(?!\=)',               "EQ"),
    (r'\*\*=',                  "POWAS"),
    (r'\+=',                    "ADDAS"),
    (r'\*=',                    "MULAS"),
    (r'-=',                     "SUBAS"),
    (r'/=',                     "DIVAS"),
    (r'%=',                     "MODAS"),
    (r'\->',                    "ARROW"),
    (r'\+\+',                   "INCR"),
    (r'\-\-',                   "DECR"),
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    
    # KEYWORD
    (r'\bvar\b',                "VAR"),
    (r'\blet\b',                "LET"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\.',                     "TITIK"),
    (r'\bformat\b',             "FORMAT"),
    (r'\bconst\b',              "CONST"),
    (r'\bnew\b',                "NEW"),
    (r'\bint\b',                "TYPE"),
    (r'\bstr\b',                "TYPE"),
    (r'\bfloat\b',              "TYPE"),
    (r'\bcomplex\b',            "TYPE"),
    (r'\blist\b',               "TYPE"),
    (r'\btuple\b',              "TYPE"),
    (r'\bset\b',                "TYPE"),
    (r'\bthrow\b',              "THROW"),
    (r'\delete\b',              "DELETE"),
    (r'\bwith\b',               "WITH"),
    (r'\w+[.]\w+',              "KARTITIK"),
    (r'\,',                     "COMMA"),
    (r'\bconstructor\b',        "CONSTRUCTOR"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\bswitch\b',             "SWITCH"),
    (r'\bcase\b',               "CASE"),
    (r'\bdefault\b',            "DEFAULT"),
    (r'\btry\b',                "TRY"),
    (r'\bcatch\b',              "CATCH"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\bclass\b',              "CLASS"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bdo\b',                 "DO"),
    (r'\bfor\b',                "FOR"),
    (r'\bimport\b',             "IMPORT"),
    (r'\bfrom\b',               "FROM"),
    (r'\brange\b',              "RANGE"),
    (r'\bnull\b',               "NULL"),
    (r'\bfalse\b',              "FALSE"),
    (r'\btrue\b',               "TRUE"),
    (r'\bfunction\b',           "FUNC"),
    (r'\breturn\b',             "RETURN"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    
]


# teks ke token
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(teks, token_exp):
    pos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1 # posisi karakter relatif terhadap baris tempat dia berada
    line = 1 # posisi baris saat ini
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in token_exp:
            pattern, tag = t
            if line == 1:
                if pattern == newA:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == newB:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            print("ILLEGAL CHARACTER")
            print("SYNTAX ERROR")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(char,token_exp)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)

    return " ".join(tokenArray)

print(create_token("file.txt"))