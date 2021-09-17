def plus1(arr,N):
    for i in range(N-1,-1,-1):
        last = arr[i]
        last += 1
        if last > 9:
            arr[i] = 0
        else:
            arr[i] = last
            break
    else:
        arr = [1] + arr
    return arr

arr = [i for i in map(int,input().split())]
a = plus1(arr,len(arr))
print("Array after adding one : ",a)
