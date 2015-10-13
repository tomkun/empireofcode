def count_inversion(seq):
    return sum([sum([x<z for x in seq[i:]]) for i,z in enumerate(seq)])
    
def count_inversion_clean(sequence):
    c = 0
    for i,n in enumerate(sequence):
        for x in sequence[i:]:
            if x<n:
                c+=1
    return c

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
