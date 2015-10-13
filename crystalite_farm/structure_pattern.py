#This probably can be done more elegantly with dicts instead of tuples

from string import ascii_lowercase, ascii_uppercase

def check_structure(pattern, structure, pattern_level=2):
    # print(structure)
    table = {
        2:(parse_bin, {('1','L'), ('0', 'D')}),
        3:(parse_tenary, {('2', 'U'), ('1','L'), ('0', 'D')}),
        4:(parse_quater, {('3', 'S'), ('2', 'U'), ('1','L'), ('0', 'D')}),
    }
    
    parse_struct, valid = table[pattern_level]
    pttrn = int2base(pattern,pattern_level).rjust(len(structure), '0')
    
    if len(pttrn) > len(structure):
        return False
    struct = parse_struct(structure)
    out = set(zip(pttrn, struct))
    return out.symmetric_difference(valid).issubset(valid)
    
def parse_bin(string):
    entry = string.lower()
    return ''.join('L' if x in ascii_lowercase else 'D' for x in entry)
    
def parse_tenary(string):
    return ''.join('L' if x in ascii_lowercase else
            'U' if x in ascii_uppercase else 'D' for x in string)
            
def parse_quater(string):
    return ''.join('S' if  x == ' ' else 'L' if x in ascii_lowercase else
            'U' if x in ascii_uppercase else 'D' for x in string)
            
def int2base(num, base):
    """
    Works for bases <=10.
    """
    out=''
    while True:
        if num>=base:
            out += str(num%base)
        else:
            out += str(num)
            return out[::-1]
        num = num//base
            
        

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert check_structure(42, "12a0b3e4"), "42 is the answer"
    assert not check_structure(101, "ab23b4zz"), "one hundred plus one"
    assert check_structure(0, "478103487120470129"), "Any number"
    assert check_structure(127, "Checkio"), "Uppercase"
    assert not check_structure(7, "Hello"), "Only full match"
    assert not check_structure(8, "a"), "Too short command"
    assert check_structure(5, "H2O"), "Water"
    assert not check_structure(42, "C2H5OH"), "Yep, this is not the Answer"

    # Rank 2
    assert check_structure(1823, 'CheckiO', 3), "up and down"
    assert not check_structure(1826, 'CheckiO', 3), "wrong up and down"
    assert check_structure(66431, '9z1b2c4d6a7Z', 3), "Various"

    # Rank 3
    assert not check_structure(39294315, 'Kill Them ALL', 4), "Don't kill"
    assert not check_structure(29, 'aXz', 4), "A Z"
    assert check_structure(39294442, 'Feed Them ALL', 4), "Feed them"
    assert check_structure(2385166685525, 'C3PO and 300 spartans', 4), "C3PO"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
