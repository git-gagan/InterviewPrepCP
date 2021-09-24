#Associativeness, finding prefix by comparing words consecutively 2 at a time.
def longestCommonPrefix(arr, n):
      prefix =  arr[0]
      for i in range(1,n):
          ans = ""
          word = arr[i]
          j = 0
          for letter in word:
              if j < len(prefix) and letter == prefix[j]:
                  ans += letter
                  j += 1
              else:
                  break
          prefix = ans
      return prefix if prefix else -1
    
arr = list(map(int,input().split())
print(longestCommonPrefix(arr,len(arr)))
    
