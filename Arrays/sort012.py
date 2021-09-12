#Optimized approach
def fun(arr,n):
    count0, count1, count2 = 0,0,0
    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
    for i in range(n):
        if count0:
            arr[i] = 0
            count0 -= 1
        elif count1:
            arr[i] = 1
            count1 -= 1
        else:
            arr[i] = 2
            count2 -= 1
    print(arr)

#Dutch National Flag Problem (4 regions)
def fun2(arr,n):
    low = 0
    mid = 0
    high = n - 1
    #Iterate in the array and shrink the mid - high (unknown range) where 1 to low is for 0's
    #low to mid is for 1's and mid to high is for unknown, high to n is for 2's
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    print("Final Array : ",arr)

arr = list(map(int,input().split()))
fun2(arr,len(arr))
