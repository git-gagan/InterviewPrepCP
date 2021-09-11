def fun(A,N):   
    #Using HAshMap 
    """mapping = {}
    for i in range(N):
        mapping[A[i]] = mapping.get(A[i],0) + 1
        if mapping[A[i]] > N/2:
            return A[i]
    return -1"""
    
    #Using Sorting
    """
    A.sort()
    count = 1
    ele = A[0]
    if N == 1:
        return ele
    for i in range(1,N):
        if ele == A[i]:
            count += 1
            if count > N/2:
                return ele
        else:
            ele = A[i]
            count = 1
    return -1
    """
    
    #Moore Voting algorithm
    #(For majority element we can cancel out non-majority elements and still get majority one)
    index = 0
    count = 0
    for i in range(N):
        if A[i] == A[index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            index = i
            count = 1
    count = 0
    for i in range(N):
        if A[i] == A[index]:
            count += 1
    if count > N/2:
        return A[index]
    return -1

A = list(map(int,input().split()))
print(fun(A,len(A)))