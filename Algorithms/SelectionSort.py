#Selection Sort is another simple algorithm for sorting where at every iteration the smallest element is selected and swapped with the first place in same array.
#Complexity :- O(n^2)

def select(arr, i):
    index = i
    for ele in range(i,len(arr)):
        if arr[ele] < arr[index]:
            index = ele
    return index

def selectionSort(arr,n):
    j = 0
    while j < n:
        index = select(arr,j)
        arr[j], arr[index] = arr[index],arr[j]
        j += 1
    return arr
  
 arr = [int(i) for i in input().strip().split()]
 print(selectionSort(arr,len(arr)))
