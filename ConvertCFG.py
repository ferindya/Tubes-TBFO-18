from CFGTOCNF import *
def cfgtocnf(CFG):
    hasil = replaceTerminal(simplyfyVariabel(removeProduction(addS0(CFG))))
    return hasil

CFG = readGrammar("grammar.txt")
print(cfgtocnf(CFG))