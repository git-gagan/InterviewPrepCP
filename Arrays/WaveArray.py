#Array is already sorted
#Else just check if elements on even positions are greater than elements on odd positions

def convertToWave(arr,N):
    i = 0
    while i < N:
        if i+1 == N:
            break
        arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 2
    return arr
  
arr = map(int,input().split())
print(convertToWave(arr,len(arr))
