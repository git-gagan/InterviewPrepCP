#Approach 1:- Brute force, Iterate and using in

#Approach 2:- Using set

#Approach 3:- Sorting and compare

#Approach 4:- Using HashMap
def removeDups(S):
		dicti = {}
		ans = ""
		for i in range(len(S)):
		    dicti[S[i]] = dicti.get(S[i],0) + 1
		    if dicti[S[i]] > 1:
		        dicti[S[i]] -= 1
		        continue
		    ans += S[i]
		return ans
  
S = input()
print(removeDups(S))
