import itertools

left, right = 0, 1
variabelsJar = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4",
"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5"]
#fungsi untuk cek apakah unit atau bukan
def isUnit(rule, variabels):
    if rule[left] in variabels and rule[right][0] in variabels and len(rule[right]) == 1:
        return True 
    else:
        return False 
def isSimple(K,V,rule):
    if rule[left] in V and rule[right][0] in K and len(rule[right]) == 1:
        return True 
    else:
        return False 

#menambahkan S0->S ke aturan 
def addS0(productions,variabels):
    variabels.append('S0')
    return [('S0', [variabels[0]])] + productions

#menghilangkan variabel yang terdiri atas terminal dan non terminal
def setupDict(productions, variabels, term):
    result = {}
    for production in productions:
        if production[left] in variabels and production[right][0] in term and len(production[right]) == 1:
            result[production[right][0]] = production[left]
    return result 

#delete non unitary rules 
def deletenonUitary(productions, variabels):
    result = []
    for production in productions:
        r = len(production[right])
        if(r <= 2):
            result.append(production)
        else:
            l = variabelsJar.pop(0)
            variabels.append(l+'1')
            result.append((production[left], [production[right][0]]+[l+'1']))
            for i in range(1,r-2):
                val, val2 = l+str(i), l+str(i+1)
                variabels.append(val2)
                result.append((val, [production[right][i], val2]))
            result.append( (l+str(r-2), production[right][r-2:r]) )
    return result 
#menghapus yang mengandung variabel dan terminal 

def unit_routine(rules,variabels):
    unitaries, result = [], []
    for rule in rules:
        if(isUnit(rule, variabels)):
            unitaries.append((rule[left], rule[right][0]))
        else:
            result.append(rule)
    for uni in unitaries:
        for arule in rules:
            if uni[right]==arule[left] and uni[left]!=arule[left]:
                result.append((uni[left],arule[right]))
    return result 





def CFGtoCNF(productions, variabels, terminals, variabelsJar):
    productions = addS0(productions,variabels)
    #menghilangkan rules yang mengandung terminal sekaligus 
    newProductions = []
    dictionary = setupDict(productions, variabels, terminals)
    for production in productions:
        if isSimple(terminals,variabels,production):
            newProductions.append(production)
        else:
            for term in terminals:
                for index, value in enumerate(production[right]):
                    if term == value and not term is dictionary:
                        dictionary[term] = variabelsJar.pop()
                        variabels.append(dictionary[term])
                        newProductions.append((dictionary[term], [term]))
                        production[right][index] = dictionary[term]
                    elif term == value:
                        production[right][index] = dictionary[term]
            newProductions.append((production[left], production[right]))
    productions = newProductions
    productions = deletenonUitary(productions, variabels)
    result = unit_routine(productions, variabels)
    temp = unit_routine(result, variabels)
    j = 0
    while result != temp and j < 1000:
	    result = unit_routine(temp, variabels)
	    temp = unit_routine(result, variabels)
	    j+=1
    
    productions = result

    return productions

    
    
def loadModel(modelPath):
	file = open(modelPath).read()
	K = (file.split("Variabels:\n")[0].replace("Terminals:\n","").replace("\n",""))
	V = (file.split("Variabels:\n")[1].split("Productions:\n")[0].replace("Variabels:\n","").replace("\n",""))
	P = (file.split("Productions:\n")[1])

	K = K.replace('  ',' ').split(' ')
	V = V.replace('  ',' ').split(' ')
	newP = []
	rawRules = P.replace('\n','').split(';')
	for rule in rawRules:
		lhs = rule.split(' -> ')[0].replace(' ','')
		rhs = rule.split(' -> ')[1].split(' | ')
		for term in rhs:
			newP.append( (lhs, term.split(' ')) )

	return K, V, newP

def displayCNF(rules):
	dictionary = {}
	for rule in rules:
		if rule[left] in dictionary:
			dictionary[rule[left]] += ' | '+' '.join(rule[right])
		else:
			dictionary[rule[left]] = ' '.join(rule[right])
	result = ""
	for key in dictionary:
		result += key+" -> "+dictionary[key]+"\n"
	return result

def prodToDict(productions):
	dictionary = {}
	for production in productions :
		if(production[left] in dictionary.keys()):
			dictionary[production[left]].append(production[right])
		else :
			dictionary[production[left]] = []
			dictionary[production[left]].append(production[right])
	return dictionary
