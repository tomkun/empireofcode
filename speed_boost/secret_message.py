from string import ascii_uppercase as uppercase
def find_message(text):
    """Find a secret message"""
    return ''.join(x for x in text if x in uppercase)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

    print("Earn cool rewards by using the 'Check' button!")
