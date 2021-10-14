def searchfirst(start,end,v,x):
    while start <= end:
        mid = (start + end)//2
        if v[mid] > x:
            end = mid - 1
        elif v[mid] < x:
            start = mid + 1
        else:
            if mid == 0 or v[mid] != v[mid-1]:
                return mid
            else:
                end = mid - 1
    return -1
        
def searchlast(start,end,v,x):
    while start <= end:
        mid = (start + end)//2
        if v[mid] > x:
            end = mid - 1
        elif v[mid] < x:
            start = mid + 1
        else:
            if mid == len(v)-1 or v[mid] != v[mid+1]:
                return mid
            else:
                start = mid + 1
    return -1
        
def indexes(v, x):
    start = 0
    end = len(v) - 1
    first = self.searchfirst(start,end,v,x)
    last = self.searchlast(start,end,v,x)
    return first,last
  
v = list(map(int,input().split()))
x = int(input())
print(indexes(v,x))
      
   
