#Approach 1 : - Sort both and compare character by character

#Approach 2 : - Use hashmap, increment and decrement.
def isAnagram(a,b):
      mapping = {}
      for i in a:
          mapping[i] = mapping.get(i,0) + 1
      for i in b:
          if i in mapping:
              mapping[i] -= 1
              if mapping[i] == 0:
                  del mapping[i]
          else:
              return False
      return True if not len(mapping) else False
 
a,b = input().split()
print(isAnagram(a,b))
    
