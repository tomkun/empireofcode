VOWELS = "aeiouy"

CONSONANT, VOWEL, VOWEL_AFTER = range(3) 

def bird2human(word):
    out = []
    last = None
    for letter in word:
        if last is None:
            out.append(letter)
            last = VOWEL if letter in VOWELS else CONSONANT
        elif last is VOWEL:
            last = VOWEL_AFTER
            continue
        elif last is VOWEL_AFTER:
            last = None
            continue
        elif last is CONSONANT:
            last = None
            continue
        
    return ''.join(out)
    
def translate(phrase):
    # print(bird2human(phrase.split(" ")[0]))
    return ' '.join([bird2human(x) for x in phrase.split(' ')])
            
            


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

