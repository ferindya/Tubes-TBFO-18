import sys
import re

# list token untuk syntax ke token
token_exp = [
    (r'[ \t]+',                 None),
    (r'#[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\n',                     "NEWLINE"),
    (r'\(',                     "KBKI"), # Kurung Biasa Kiri
    (r'\)',                     "KBKA"), # Kurung Biasa Kanan
    (r'\[',                     "KSKI"), # Kurung Siku Kiri
    (r'\]',                     "KSKA"), # Kurung Siku Kanan
    (r'\{',                     "KKKI"), # Kurung Kurawal Kiri
    (r'\}',                     "KKKA"), # Kurung Kurawal Kanan
    (r'\;',                     "TITIKOMA"),
    (r'\"',                     "PETIKDUA"),
    (r'\'',                     "PETIKSATU"),
    (r'\:',                     "TITIKDUA"),
    (r'\*\*=',                  "POWAS"),
    (r'\+=',                    "ADDAS"),
    (r'\*=',                    "MULAS"),
    (r'-=',                     "SUBAS"),
    (r'/=',                     "DIVAS"),
    (r'%=',                     "MODAS"),
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    (r'\*\*',                   "POW"),
    (r'\/\/',                   "FLOORDIV"),
    (r'\=(?!\=)',               "EQ"),
    (r'\==',                    "ISEQ"),
    (r'<=',                     "LEQ"),
    (r'>=',                     "GEQ"),
    (r'!=',                     "NEQ"),
    (r'&&',                     "AND"),
    (r'||',                     "OR"),
    (r'!',                      "NOT"),
    (r'^',                      "XOR"),
    (r'<<',                     "LEFTSHIFT"),
    (r'>>',                     "RIGHTSHIFT"),
    (r'>>>',                    "UNRIGHTSHIFT"),
    (r'\->',                    "ARROW"),
    (r'\bformat\b',             "FORMAT"),
    (r'\band\b',                "AND"),
    (r'\bor\b',                 "OR"),
    (r'\bnot\b',                "NOT"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\brange\b',              "RANGE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bfalse\b',              "FALSE"),
    (r'\btrue\b',               "TRUE"),
    (r'\bclass\b',              "CLASS"),
    (r'\breturn\b',             "RETURN"),
    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\delete\b',              "DELETE"),
    (r'\bconstructor\b',        "CONSTRUCTOR"),
    (r'\bwith\b',               "WITH"),
    (r'\bswitch\b',             "SWITCH"),
    (r'\bcase\b',               "CASE"),
    (r'\bdefault\b',            "DEFAULT"),
    (r'\btry\b',                "TRY"),
    (r'\bcatch\b',              "CATCH"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\bdo\b',                 "DO"),
    (r'\bconst\b',              "CONST"),
    (r'\bnull\b',               "NULL"),
    (r'\,',                     "COMMA"),
    (r'\w+[.]\w+',              "KARTITIK"),
    (r'\.',                     "TITIK"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
    (r'\bvar\b',              "VAR"),
    (r'\blet\b',              "LET"),
    (r'\bcontinue\b',          "CONTINUE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'\.',                     "TITIK"),
    (r'\bformat\b',             "FORMAT"),
    (r'\(',                     "KBKI"),
    (r'\)',                     "KBKA"),
    (r'\bcons\b',          "CONTINUE"),
    (r'\[',                     "KSKI"), 
    (r'\]',                     "KSKA"),
    (r'\;',                     "TITIKOMA"),
    (r'\bnew\b',                     "NEW"),
    (r'\bint\b',                "TYPE"),
    (r'\bstr\b',                "TYPE"),
    (r'\bfloat\b',              "TYPE"),
    (r'\bcomplex\b',            "TYPE"),
    (r'\blist\b',               "TYPE"),
    (r'\btuple\b',              "TYPE"),
    (r'\bset\b',                "TYPE"),
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    (r'\*\*',                    "POW"),
    (r'\/\/',                    "FLOORDIV"),
    (r'\bnot\b',                "NOT"),
    (r'\bthrow\b',               "THROW")
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

def createToken(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(char,token_exp)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)

    return " ".join(tokenArray)

if __name__ == "__main__":
    create_token('test.txt')