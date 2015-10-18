from math import sqrt, pi

def simple_areas(*args):
    if len(args) == 1:
        return (pi/4)*args[0]**2
    elif len(args) == 2:
        return args[0]*args[1]
    else:
        s = sum(args)/2
        a,b,c = args
        return sqrt(s*(s-a)*(s-b)*(s-c))