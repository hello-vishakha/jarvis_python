print("The dimension : " + str(N))
  
# using list comprehension
# matrix creation of n * n
res = [list(range(1 + N * i, 1 + N * (i + 1)))
                            for i in range(N)]
  
# print result
print("The created matrix of N * N: " + str(res))
