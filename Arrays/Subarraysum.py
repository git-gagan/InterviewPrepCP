#Sliding Window Approach
def fun1(s,n,arr):
    my_sum = 0
    curr_index = 0
    starting_index = 0
    while curr_index <= n:
        if my_sum > s:
            my_sum -= arr[starting_index] 
            starting_index += 1
        elif my_sum == s:
            return starting_index + 1, curr_index
        elif curr_index < n:
            my_sum += arr[curr_index]
            curr_index += 1
    return -1

#Prefix Sum
def fun2(s,n,arr):
    map = {}
    my_sum = 0
    for i in range(n):
        print(map)
        print(my_sum)
        my_sum += arr[i]
        if my_sum == s:
            return 1,i+1
        if my_sum - s in map:
            return map[my_sum-s]+1,i+1
        map[my_sum] = i+1
    return -1

#Approach 3 is naive Brute Force with time complexity O(n^2)

a = list(map(int,input().split()))
subsum = int(input("Enter the subarray sum to check for : "))
print(fun2(subsum,len(a), a))