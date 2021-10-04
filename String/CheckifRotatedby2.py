#Check if a string is rotated by 2 places
def isRotated(str1,str2):
    if str1[2:] + str1[:2] == str2:
        return 1
    if str1[-2:] + str1[:-2] == str2:
        return 1
    return 0
  
str1,str2 = input().strip().split()
print(isRotated(str1,str2))
