#I seriously don't remember why haven't I simply used digits from strings module ;)
DIGITS = ''.join(str(x) for x in list(range(10)))

def three_words(words):
    split = words.split()
    for i,word in enumerate(split[:-2]):
        m = list(map(has_nums, [word, split[i+1], split[i+2]]))
        if not any(m):
            return True
    return False
            
def has_nums(word):
    return any(x in word for x in DIGITS)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert three_words("Hello World hello"), "Hello"
    assert not three_words("He is 123 man"), "123 man"
    assert not three_words("1 2 3 4"), "Digits"
    assert three_words("bla bla bla bla"), "Bla Bla"
    assert not three_words("Hi"), "Hi"
