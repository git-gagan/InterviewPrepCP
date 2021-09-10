#Equlibrium Point 

#Tricky Approach
def fun(A,N):
    if N == 1:
        return 1
    my_sum = sum(A) - A[0]
    left = 0
    right = my_sum
    for i in range(1,N):
        element = A[i-1]
        left += element
        right -= A[i]
        if left == right:
            return i + 1
    return -1

#Prefix Sum approach
def fun(A,N):
    left_sum = [A[0]]
    right_sum = [A[N-1]]
    for i in range(1,N):
        left_sum.append(left_sum[i-1] + A[i])
        right_sum.append(right_sum[i-1] + A[N-1-i])
    print(left_sum,right_sum)
    for i in range(N):
        if left_sum[i] == right_sum[N-1-i]:
            return i+1
    return -1

A = list(map(int,input().split()))
print(fun(A,len(A)))