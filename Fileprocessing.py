import sys 
import re

# list token untuk syntax ke token
exp_token = [
    (r'[ \t]+',                 None),
    (r'#[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    
    # Integer dan String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    
    # Delimiter
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

    # Operator
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
    
    # KEYWORD
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
]

# TEKS KE TOKEN
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(text, exp_token):
    pos = 0
    currentPos = 0
    line = 1
    tokens = []
    while pos < len(text):
        if text[pos] == '\n':
            currentPos = 1
            line += 1
        match = None
        
        for t in exp_token:
            pattern, tag = t
            if line == 1:
                if pattern == newA:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == newB:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(text, pos)
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
        currentPos += 1
    return tokens

def createToken(sentence):
    file = open(sentence)
    char = file.read()
    file.close()
    
    tokens = lexer(char, exp_token)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)
        
    return " ".join(tokenArray)

if __name__ == "__main__":
    createToken('test.txt')