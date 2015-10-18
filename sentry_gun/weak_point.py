"""
    Using min() did not guarantee to return the first weakest row 
    in situations where >1 were of equal, lowest score
"""
def a(m):
 s,w=99,0
 for i,x in enumerate(m):
  if sum(x)<s:
   s,w=sum(x),i
 return w
golf=lambda m:[a(m),a(zip(*m))]