from parserCFG import *
def addS0(CFG):
    headlist = list(CFG.keys())
    bodylist = list(CFG.values())
    startsymbol = headlist[0]
    addnewrule = False
    for rules in bodylist:
        for rule in rules:
            if startsymbol in rule:
                addnewrule = True
                break 
        if addnewrule:
           break 
    if addnewrule:
        newRule = {"SNEW" : [[startsymbol]]}
        newRule.update(CFG)
        CFG = newRule
    return CFG 


def removeProduction(CFG):
    valid = True 
    while valid:
        unitproduction = {}
        valid = False 
        for head, body in CFG.items():
            for rule in body:
                if len(rule) == 1 and isVar(rule[0]):
                    valid = True
                    if head not in unitproduction.keys():
                        unitproduction[head] = [[rule[0]]]
                    else:
                        unitproduction[head].append([rule[0]])
        for headunit, bodyunit in unitproduction.items():
            for ruleunit in bodyunit:
                for head, body in CFG.items():
                    if(len(ruleunit) == 1) and head == ruleunit[0]:
                        newRule = {headunit : body}
                        if headunit not in CFG.keys():
                            CFG[headunit] = body
                        else:
                            for rule in body:
                                if rule not in CFG[headunit]:
                                    CFG[headunit].append(rule)
        for headunit,bodyunit in unitproduction.items():
            for ruleunit in bodyunit:
                if len(ruleunit) == 1:
                    CFG[headunit].remove(ruleunit)
    return CFG 


def simplyfyVariabel(CFG):
    newProduction = {}
    delProduction = {}

    j = 0
    for head, body in CFG.items():
        for rule in body:
            headsymbol = head 
            temprule = [r for r in rule]
            if len(temprule) > 2:
                while(len(temprule)) > 2:
                    newSymbol =  f"X{j}"
                    if headsymbol not in newProduction.keys():
                        newProduction[headsymbol] = [[temprule[0],newSymbol]]
                    else:
                        newProduction[headsymbol].append([temprule[0], newSymbol])
                    headsymbol = newSymbol
                    temprule.remove(temprule[0])
                    j += 1
                else: 
                    if headsymbol not in newProduction.keys():
                        newProduction[headsymbol] = [temprule]
                    else:
                        newProduction[headsymbol].append(temprule)
                    if head not in delProduction.keys():
                        delProduction[head] = [rule]
                    else:
                        delProduction[head].append(rule)
    for newhead, newbody in newProduction.items():
        if newhead not in CFG.keys():
            CFG[newhead] = newbody
        else:
            CFG[newhead].extend(newbody)
    for delhead, delbody in delProduction.items():
        for delrule in delbody:
            CFG[delhead].remove(delrule)
    return CFG


def replaceTerminal(CFG):
    newProduction = {}
    delProduction = {}
    i = 0
    j = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and isTerminal(rule[0]) and isTerminal(rule[1]):
                newSyimbolY = f"Y{i}"
                newSyimbolZ = f"Z{j}"
                if head not in newProduction.keys():
                    newProduction[head] = [[newSyimbolY,newSyimbolZ]]
                else:
                    newProduction[head].append([newSyimbolY,newSyimbolZ])
                
                newProduction[newSyimbolY] = [[rule[0]]]
                newProduction[newSyimbolZ] = [[rule[1]]]
                if head not in delProduction.keys():
                    delProduction[head] = [rule]
                else:
                    delProduction[head].append(rule)
                i += 1
                j += 1
            elif len(rule) == 2 and isTerminal(rule[0]):
                newSyimbolY = f"Y{i}"
                if head not in newProduction.keys():
                    newProduction[head] = [[newSyimbolY,rule[1]]]
                else:
                    newProduction[head].append([newSyimbolY,rule[1]])
                newProduction[newSyimbolY] = [[rule[0]]]

                if head not in delProduction.keys():
                    delProduction[head] = [rule]
                else:
                    delProduction[head].append(rule)
                
                i += 1
            elif len(rule) == 2 and isTerminal(rule[1]):
                newSyimbolZ = f"Z{j}"
                if head not in newProduction.keys():
                    newProduction[head] = [[rule[0],newSyimbolZ]]
                else:
                    newProduction[head].append([rule[0],newSyimbolZ])
                
                newProduction[newSyimbolZ] = [[rule[1]]]

                if head not in delProduction.keys():
                    delProduction[head] = [rule]
                else:
                    delProduction[head].append(rule)

                j += 1

            else:
                pass 
    for newhead,newbody in newProduction.items():
        if newhead not in CFG.keys():
            CFG[newhead] = newbody
        else:
            CFG[newhead].extend(newbody)
    for delhead, delbody in delProduction.items():
        for delrule in delbody:
             CFG[delhead].remove(delrule)
    return CFG
