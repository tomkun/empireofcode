VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
DIGITS = ''.join(str(x) for x in list(range(10)))

def striped_words(text):
    out = 0
    t = ''.join([x if x in VOWELS + CONSONANTS + DIGITS else " " if x == '.'else " " for x in text.upper() ]).split()
    for word in t:
        if len(word) <= 1 or any(x in word for x in DIGITS):
            continue
        for i, letter in enumerate(word[:-1]):
            if (letter in VOWELS and word[i+1] not in CONSONANTS) or (letter in CONSONANTS and word[i+1] not in VOWELS):
                break
        else:
            out+=1
    return out

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert striped_words("My name is ...") == 3, "All words are striped"
    assert striped_words("Hello world") == 0, "No one"
    assert striped_words("A quantity of striped words.") == 1, "Only of"
    assert striped_words("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
