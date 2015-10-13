import re;golf=lambda r:sum(int(n)+(ord(l)-65)*9for l,n in re.findall('[A-Z][1-9]',r))

# golf=lambda r:sum(int(r[i+1])+(ord(l)-65)*9for i,l in enumerate(r[:-1])if 64<ord(l)<91and 48<ord(r[i+1])<58) ## without regex

# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert golf("ASDA1,BB22D01C1") == 31
    # assert golf("B1,C2,D3") == 60
