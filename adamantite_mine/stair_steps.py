"""
The long way && explanation

def golf(numbers):
    s=0
    while len(numbers)>1:
        a,b = numbers[:2]
        
        ## if the closest step is a positive number, we want to take it every time
        ## otherwise we check whether picking or skipping it gives us a higher score overall
        if a>0 or sum(numbers[:-1])>sum(numbers[1:]):     
            s+=a
            numbers=numbers[1:]
        else:
            s+=b
            numbers=numbers[2:]

    ## when we arrive on the last step, we can either take it if it's positive
    ## or skip it altogether
    if numbers and numbers[0]>0:
        s+=numbers[0]
    return s

"""

g=lambda n,s=0:s if not n else s+max(0,n[0])if len(n)==1else g(n[1:],s+n[0])if n[0]>0 or sum(n[:-1])>sum(n[1:])else g(n[2:],s+n[1])
golf=g