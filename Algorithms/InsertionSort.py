#Insertion Sort is a simple Algorithm where we pick values from the unsorted part of the array and move it to sorted part.
#Worst case complexity :- O(n^2)

#Insert fucntion to do proper swapping of our unsorted element to put it into its sorted place
def insert(alist, index, n):
    for i in range(index-1,-1,-1):
        if alist[index] < alist[i]:
            alist[index], alist[i] = alist[i], alist[index]
            index -= 1

#Function to sort the list using insertion sort algorithm.    
def insertionSort(alist, n):
    #code here
    i = 0
    while i < n-1:
        insert(alist,i+1,n)
        i += 1
    return alist
  
alist = [int(i) for i in input().spliy()]
print(insertionSort(alist,len(alist)))
