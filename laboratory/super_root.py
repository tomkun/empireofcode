# from __future__ import print_function

def super_root(number):
    hi = get_sane_high(number)
    low = number**(1/number)
    c = (hi+low)/2.0
    
    while abs((c**c)-number)>0.001:
        if c**c > number:
            hi = c
            c = (c+low)/2.0
        else:
            low = c
            c = (c+hi)/2.0
    return c

def get_sane_high(n):
    inc = 0.000000001 * n
    c = inc
    while c**c<n:
        c*=2
    return c

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False

    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
