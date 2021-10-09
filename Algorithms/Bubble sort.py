#Simplest sorting algorithms using adjacent element comparison 
#worst case is O(n^2)
#Best case is O(n)

def bubbleSort(arr, n):
    for i in range(n-1):
        swapped = False
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr 
  
arr = list(map(int,input().split()))
print(bubbleSort(arr,len(arr)))
