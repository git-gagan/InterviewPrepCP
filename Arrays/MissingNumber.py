def missing(array,n):    
    #Approach 1 (Summation)
    #return n*(n+1)//2 - sum(array)
    
    #Approach 2 (XOR)
    a = 0
    for i in range(1,n+1):
        a = a ^ i
    b = 0
    for j in range(n-1):
        b = b ^ array[j]
    return a ^ b

arr = list(map(int,input().split()))
n = int(input("Enter the size: "))
print(missing(arr,n))