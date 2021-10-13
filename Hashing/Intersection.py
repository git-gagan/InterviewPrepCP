def NumberofElementsInIntersection(a, b, n, m):
      #Using Hash
      count = 0
      seta = {ele for ele in a}
      for ele in b:
          if ele in seta:
              seta.remove(ele)
              count +=1
      return count

      #Another approach is to use dicts in case of Duplicacy
      #Brtue Force can also be applied
      #Two pointer approach
      #Sorting and using binary search
 
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
n,m = map(int,input().split())
print(NumberofElementsInIntersection(a, b, n, m))
