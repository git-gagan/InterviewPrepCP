def rotateArr(A,D,N):
    #Approach 1 (using reverse())
    if D > N:
        D = D%N
    def reverse(start,end):
        while start < end:
            A[start],A[end-1] = A[end-1],A[start]
            start += 1
            end -= 1
        
    reverse(0,N)
    reverse(0,N-D)
    reverse(N-D,N)

    #Approach 2 (Pop Last element and unshift())

    #Approach 3 (Create a new array and append accordingly)

D = int(input("Digits: "))
A = list(map(int,input().split()))
rotateArr(A,D,len(A))
print(A)