#Hashing Approach
def check(A,B,N):
    mapping = {}
    for i in A:
        mapping[i] = mapping.get(i,0)+1
    for i in B:
        if i in mapping:
            mapping[i] -= 1
            if mapping[i] < 0:
                return False
            continue
        return False
    return True
  

#One of the approaches is to sort both arrays and do element by element comparison.
