#Naive Approach :- Using linear search for element by element comparison.

#Optimized
def searchInsertK(self, Arr, N, k):
      start = 0
      end = N - 1
      while start <= end:
          mid = (start + end)//2
          if Arr[mid] == k:
              return mid
          elif Arr[mid] < k:
              start = mid + 1
          else:
              end = mid - 1
      return start

Arr = [i for i in map(int,input().strip().split())]
K = int(input())
searchInsertK(Arr,len(Arr),K)
