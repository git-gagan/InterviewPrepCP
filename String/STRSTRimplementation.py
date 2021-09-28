def strstr(s,x):
    i,j,index = 0,0,-1
    while i < len(s):
        if s[i] != x[j]:
            j,index = 0,-1
        else:
            if index == -1:
                index = i
            j += 1
            if j == len(x):
                return index
        i += 1
    return -1

s = input()
x = input()
print(strstr(s,x))
