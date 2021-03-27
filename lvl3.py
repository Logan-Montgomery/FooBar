#level 3 problem 1
# Write a function solution(l) that takes a list of positive integers l and counts
# the number of "lucky triples" of (li, lj, lk) where the list indices meet the
# requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The
# elements of l are between 1 and 999999 inclusive.  The solution fits within a 
# signed 32-bit integer. Some of the lists are purposely generated without any
# access codes to throw off spies, so if no triples are found, return 0. 
    
# For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6],
# making the solution 3 total.
    
##Solution never completed, worked on most tes cases##
##but ran out of time to complete the mission.##
##NOTE: Prob a better way to do matrix arithmatic than this##
def solution6(l):
    lst = []
    matrix = [] * len(lst)
    for i in range (0,len(l)):
        for j in range(0,len(l)):
            if j > i and l[j] % l[i] == 0:
                #print((l[j],l[i]))
                if j > i:
                    lst.append(1)
            else: lst.append(0)
    i=0
    while i<len(lst):
        matrix.append(lst[i:i+len(l)])
        i+= len(l) 
        
    n = len(l)
    m = len(l)
    result = [0] * n
    for x in range (n):
        result[x] = [0] * m
    #print(result)
              
   # iterate through rows of X
    for i in range(len(matrix)):
   # iterate through columns of Y
        for j in range(len(matrix[0])):
       # iterate through rows of Y
            for k in range(len(matrix)):
                result[i][j] += matrix[i][k] * matrix[k][j]
        
    final = sum(result,[])
    #print(sum (final))
    #print(matrix)  
    return(sum(final))  