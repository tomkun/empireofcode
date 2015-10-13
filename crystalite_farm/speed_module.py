FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"

"""
This is probably the worst, most unintentionally obfuscated python code I've ever written.
But it works, so eh.
"""

# TODO cleaner rewrite

def tell_number(number):
    if number == 0:
        return 'zero'
    out = ' thousand '.join([parse(x[::-1]) for x in triplet(str(number).lstrip('-')[::-1]) if x][::-1]).strip()
    return out if number >0 else ' '.join(['minus', out])

def triplet(l):
    return [l[i:i+3] for i in range(0, len(l), 3)]
    
def parse(num):
    return (FIRST_TEN[int(num[0])-1]+" hundred " if len(num)>2 and int(num[0]) >0 else '') + tens(int(num[-2:]))
    
def tens(n):
    if n == 0 :
        return ''
    if n < 10:
        return FIRST_TEN[n-1]
    if n < 20:
        return SECOND_TEN[n-10]
    a,b = str(n)
    return OTHER_TENS[int(a)-2] + ((" "+ FIRST_TEN[int(b)-1]) if b!='0' else '')

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert tell_number(12) == "twelve", "12"
    assert tell_number(77) == "seventy seven", "77"
    assert tell_number(34) == "thirty four", "34"
    assert tell_number(52) == "fifty two", "52"
    assert tell_number(4) == 'four', "1st example"
    assert tell_number(133) == 'one hundred thirty three', "2nd example"
    assert tell_number(12) == 'twelve', "3rd example"
    assert tell_number(101) == 'one hundred one', "4th example"
    assert tell_number(212) == 'two hundred twelve', "5th example"
    assert tell_number(40) == 'forty', "6th example"
    assert not tell_number(212).endswith(' '), "Dont forget strip whitespaces at the end of string"

    # Rank 2
    assert tell_number(-133) == 'minus one hundred thirty three', "Minus"
    assert tell_number(0) == 'zero', "Zero"

    # Rank 3
    assert tell_number(42512) == 'forty two thousand five hundred twelve', tell_number(42512)
    assert tell_number(42000) == 'forty two thousand', "42 many"
    assert (tell_number(-999999) ==
            "minus nine hundred ninety nine thousand nine hundred ninety nine"), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")
