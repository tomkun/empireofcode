from string import ascii_uppercase as letters

def count_ingots(report):
    return sum(get_num(num) for num in report.split(","))
    
def get_num(val):
    return int(val[1])+(letters.index(val[0])*9)
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_ingots("A2,B1") == 12, "One and eleven"
    assert count_ingots("A1,A1,A1") == 3, "One, two, three"
    assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
    assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"
