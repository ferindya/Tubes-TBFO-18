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
    (r'\(',                     "KBKI"), # Kurung Biasa Kiri
    (r'\)',                     "KBKA"), # Kurung Biasa Kanan
    (r'\[',                     "KSKI"), # Kurung Siku Kiri
    (r'\]',                     "KSKA"), # Kurung Siku Kanan
    (r'\{',                     "KKKI"), # Kurung Kurawal Kiri
    (r'\}',                     "KKKA"), # Kurung Kurawal Kanan
    (r'\;',                     "TITIKOMA"),
    (r'\:',                     "TITIKDUA"),
    (r'\n',                     "NEWLINE"),
    (r'\"',                     "PETIKDUA"),
    (r'\'',                     "PETIKSATU"),

    # Operator
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    (r'\*\*',                   "POW"),
    (r'\/\/',                   "FLOORDIV"),
    (r'!',                      "NOT"),
    (r'\==',                    "ISEQ"),
    (r'<=',                     "LEQ"),
    (r'>=',                     "GEQ"),
    (r'!=',                     "NEQ"),
    (r'&&',                     "AND"),
    (r'||',                     "OR"),
    (r'^',                      "XOR"),
    (r'<<',                     "LEFTSHIFT"),
    (r'>>',                     "RIGHTSHIFT"),
    (r'>>>',                    "UNRIGHTSHIFT"),
    (r'\=(?!\=)',               "EQ"),
    (r'\*\*=',                  "POWAS"),
    (r'\+=',                    "ADDAS"),
    (r'\*=',                    "MULAS"),
    (r'-=',                     "SUBAS"),
    (r'/=',                     "DIVAS"),
    (r'%=',                     "MODAS"),
    (r'\->',                    "ARROW"),
    
    
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
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
    (r'\breturn\b',             "RETURN"),
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