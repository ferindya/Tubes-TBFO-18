# CATATAN:
# Head pertama akan menjadi Start Symbol
# Tidak mengandung Useless Production (tidak terdapat Variables yang tidak dapat diderivasi 
# menjadi string dan tidak terdapat Productions yang tidak muncul pada derivasi string)
# Tidak mengandung Null Production (tidak terdapat Variables yang menghasilkan epsilon, 
# kecuali pada Start Symbol)

def readGrammar(fileName):
    file = open(fileName, "r")
    cfg = {}

    row = file.readline()
    while row != "":
        head, body = row.replace("\n", "").split(" -> ")
        
        if head not in cfg.keys():
            cfg[head] = [body.split(" ")]
        else:
            cfg[head].append(body.split(" "))

        row = file.readline()

    file.close()

    return cfg

def isTerminal(string):
    listTerminal = [
        "VAR",
        "LET",
        "INCR",
        "DECR",
        "CONTINUE",
        "BREAK",
        "STRING",
        "TITIK",
        "KBKI",
        "KBKA",
        "CONST",
        "KSKI",
        "KSKA",
        "TITIKOMA",
        "NEW",
        "TYPE",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "MOD",
        "POW",
        "NOT",
        "THROW",
        "DELETE",
        "ISEQ",
        "LEQ",
        "L",
        "NEQ",
        "GEQ",
        "G",
        "AND",
        "OR",
        "KKKI",
        "KKKA",
        "KARTITIK",
        "COMMA",
        "TITIKDUA",
        "EQ",
        "INT",
        "IF",
        "ELSE",
        "ADDAS",
        "MULAS",
        "SUBAS",
        "POWAS",
        "DIVAS",
        "MODAS",
        "SWITCH",
        "CASE",
        "DEFAULT",
        "TRY",
        "CATCH",
        "FINALLY",
        "WHILE",
        "DO",
        "FOR",
        "NEWLINE",
        "NULL",
        "TRUE",
        "FALSE",
        "ARROW",
        "PETIKSATU",
        "PETIKDUA",
        "ID",
        "RETURN"
    ]
    
    return string in listTerminal

def isVar(string):
    return not isTerminal(string)