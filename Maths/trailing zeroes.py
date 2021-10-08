def trailingZeroes(N):
    #Calculate the prime factors 2 and 5 cause they only lead to trailing zeroes.
    if N < 5:
        return 0
      count = 0
    #Keep dividing the number by 5 till it becomes less than 5 and add the quotient
    while N >= 5:
        N //= 5
        count += N
      return count
    
print(trailingZeroes(int(input())))
