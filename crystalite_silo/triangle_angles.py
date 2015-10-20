from math import acos, degrees

def angles(a, b, c):
    angle_math = lambda a,b,c:round(degrees(acos((a**2 + b**2 - c**2)/(2*a*b))),0)
    try:
        angles = [angle_math(*x) for x in ((a,b,c), (b,c,a), (c,a,b))]
    except ValueError:
        return [0,0,0]
    if 0 in angles:
        return [0,0,0]
    return sorted(angles)