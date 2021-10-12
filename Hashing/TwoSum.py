def keypair(A, N, X):
      #brute Force using two loops
      """
      for i in range(N):
          for j in range(i+1,N):
              if A[i]+A[j] == X:
                  return True
      return False      
      """
      #Another approach is sorting and 2 pointer approach
      #Optimized approach using dicts corressponding to hash tables
      """
      mapping = {}
      for ele in A:
          mapping[ele] = mapping.get(ele,0) + 1
      for ele in A:
          mapping[ele] -= 1
          if mapping[ele] <= 0:
              del mapping[ele]
          if X-ele in mapping:
              return True
      return False
      """
      #Optimized approach using dicts corressponding to hash tables
      sets = set()
      for ele in A:
          if (X - ele) in sets:
              return True
          sets.add(ele)
      return False
 
A = list(map(int,input().split()))
X = int(input())
print(keypair(A,X,len(A)))
    
