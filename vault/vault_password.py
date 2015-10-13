import re
golf=lambda p:bool(re.findall('(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{10,}',p))
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    golf('A1213pokl') == False
    golf('bAse730onE') == True
    golf('asasasasasasasaas') == False
    golf('QWERTYqwerty') == False
    golf('123456123456') == False
    golf('QwErTy911poqqqq') == True