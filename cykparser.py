def CYKParser(CNF, string):
    S = string.split(" ")
    N = len(S)
    T = [[set([]) for j in range(N)] for i in range(N)]

    for j in range(N):
        for first, tail in CNF.items():
            for rule in tail:
                if len(rule) == 1 and rule[0] == S[j]:
                    T[j][j].add(first)

        for i in range(j, -1, -1):
            for k in range(i, j):
                for first, tail in CNF.items():
                    for rule in tail:
                        if len(rule) == 2 and rule[0] in T[i][k] and rule[1] in T[k + 1][j]:
                            T[i][j].add(tail)
                            print(T[i][j])
    return len(T[0][N - 1]) != 0
