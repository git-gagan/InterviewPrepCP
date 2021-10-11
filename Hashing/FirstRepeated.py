#Brute force approach is to use 2 loops
#Another Approach is to sort the array, sort it in temp and count occurrences using Binary Search

#Hashing Approach
def firstRepChar(s):
    hashmap = {}
    for i in s:
        hashmap[i] = hashmap.get(i,0) + 1
        if hashmap[i] > 1:
            return i
    return -1
  
print(firstRepChar(input()))

    
