#Store the pattern in a Hash map and iterate the string, if any cahr of string is present in Map, return it's index

def minIndexChar(str, pat): 
    patMap = {pat[i]:i for i in range(len(pat))}
    for index in range(len(str)):
        if str[index] in patMap:
            return index
    return -1
  
str,pat = input().split()
print(minIndexChar(str,pat))
