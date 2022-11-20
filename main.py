from CFGToCNF import *
import sys

K, V, Productions = [],[],[]


for nonTerminal in V:
	if nonTerminal in variablesJar:
		variablesJar.remove(nonTerminal)
if len(sys.argv) > 2:
	modelPath = str(sys.argv[2])
else:
	modelPath = 'cfgtocnf.txt'
K, V, Productions = loadModel( modelPath )
Productions = CFGtoCNF(Productions,V,K,variabelsJar)
cnfGram = prodToDict(Productions)
open('cnf.txt', 'w').write(displayCNF(Productions) )