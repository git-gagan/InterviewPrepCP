def leaders(A, N):
    res = []
    #Brute Force
    """
    for i in range(N-1):
        for j in range(i+1,N):
            if A[i] < A[j]:
                break
        else:
            res.append(A[i])
    """

    #Scan from right
    maxi = A[-1]
    for i in range(N-1,-1,-1):
        if A[i] >= maxi:
            maxi = A[i]
            res.append(maxi)
    return res[::-1]

A = list(map(int,input().split()))
print(leaders(A,len(A)))
