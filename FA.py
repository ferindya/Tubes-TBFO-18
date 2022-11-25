import sys
import re

# list terminal: syntax -> terminal
terminalExp = [
    (r'[ \t]+',                 None),
    (r'//[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\(',                     "KBKI"), 
    (r'\)',                     "KBKA"), 
    (r'\[',                     "KSKI"), 
    (r'\]',                     "KSKA"),
    (r'\{',                     "KKKI"), 
    (r'\}',                     "KKKA"), 
    (r'\;',                     "TITIKOMA"),
    (r'\:',                     "TITIKDUA"),
    (r'\n',                     "NEWLINE"),
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
    (r'\bvar\b',                "VAR"),
    (r'\blet\b',                "LET"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bbreak\b',              "BREAK"),
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
    (r'\.',                     "TITIK"),
    (r'\,',                     "COMMA"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    
]


# teks -> terminal
textToTerm1 = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
textToTerm2 = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(text, terminalExp):
    pos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1 # posisi karakter relatif terhadap baris tempat dia berada
    line = 1 # posisi baris saat ini
    tknn = []
    while pos < len(text):
        if text[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in terminalExp:
            pattern, tag = t
            if line == 1:
                if pattern == textToTerm1:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == textToTerm2:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(text, pos)
            if match:
                if tag:
                    token = tag
                    tknn.append(token)
                break

        if not match:
            print("ILLEGAL CHARACTER")
            print("SYNTAX ERROR")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tknn

def createToken(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tknn = lexer(char,terminalExp)
    tokenArray = []
    for token in tknn:
        tokenArray.append(token)

    return " ".join(tokenArray)

#print(createToken("file.txt"))