def hamming(n, m):
    return sum(int(x) for x in str(bin(n^m))[2:])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert hamming(117, 17) == 3, "First example"
    assert hamming(1, 2) == 2, "Second example"
    assert hamming(16, 15) == 5, "Third example"