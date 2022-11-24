# ATURAN MENULIS GRAMMAR:
# Head pertama akan menjadi Start Symbol
# Tidak mengandung Useless Production (tidak terdapat Variables yang tidak dapat diderivasi menjadi string dan tidak terdapat Productions yang tidak muncul pada derivasi string)
# Tidak mengandung Null Production (tidak terdapat Variables yang menghasilkan epsilon, kecuali pada Start Symbol)

def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    baris = file.readline()
    while baris != "":
        head, body = baris.replace("\n", "").split(" -> ")
        
        if head not in cfg.keys():
            cfg[head] = [body.split(" ")]
        else:
            cfg[head].append(body.split(" "))

        baris = file.readline()

    file.close()

    return cfg

def isTerminal(string):
    list_of_terminal = [
        "VAR",
        "LET",
        "CONTINUE",
        "BREAK",
        "STRING",
        "TITIK",
        "FORMAT",
        "KBKI",
        "KBKA",
        "CONST",
        "KSKI",
        "KSKA",
        "TITIKOMA",
        "NEW",
        "SET",
        "TYPE",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "MOD",
        "POW",
        "FLOORDIV",
        "NOT",
        "THROW",
        "DELETE",
        "ISEQ",
        "LEQ",
        "NEQ",
        "GEQ",
        "AND",
        "OR",
        "XOR",
        "LEFTSHIFT",
        "RIGHTSHIFT",
        "UNRIGHTSHIFT",
        "WITH",
        "KKKI",
        "KKKA",
        "KARTITIK",
        "COMMA",
        "TITIKDUA",
        "EQ",
        "INT",
        "CONSTRUCTOR",
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
        "CLASS",
        "WHILE",
        "DO",
        "FOR",
        "IMPORT",
        "FROM",
        "RANGE",
        "NEWLINE",
        "CONST",
        "NULL",
        "TRUE",
        "FALSE",
        "PETIKSATU",
        "ARROW",
        "PETIKSATU",
        "PETIKDUA"
    ]
    
    return string in list_of_terminal

def isVar(string):
    return not isTerminal(string)

# def is_variables(string):
#     return len(string) > 0 and string[0].isupper()

# def is_terminal(string):
#     return not is_variables(string)