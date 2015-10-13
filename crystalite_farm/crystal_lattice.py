"""
The long way && explanation

def golf(c):
    for r,d in enumerate(c[:-1]):
        for a,w in enumerate(d):
            for i,g in enumerate(w[:-1]):
                if g in[w[i+1],c[r+1][a][i]]:
                    return 0
    return 1

"""

e=enumerate
golf=lambda c:all([0in x for x in[i for s in[[[g in[w[i+1],c[r+1][a][i]]for i,g in e(w[:-1])]for a,w in e(d)]for r,d in e(c[:-1])]for i in s]])