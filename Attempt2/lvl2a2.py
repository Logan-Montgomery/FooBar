# I dont remember the eaxt problem statment,
# solution() does stu with the sum if fib numbers
###LEVEL 2.2#### 
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
def sumFib(x):
    Sum = 0
    for i in range(x+2):
        Sum += f(i)
    return Sum    
def solution(total_lambs):
    lst = []
    i = 0
    while True:
        lst.append(sumFib(i))
        if lst[i] > total_lambs:
            break 
        i += 1
    Max = len(lst)-1
    print(lst)
    
    lst2 = []
    i = 0
    while True:
        addLst = [1]
        for j in range(0,i):
            addLst.append(addLst[j]*2)
        lst2.append(sum(addLst))
        if lst2[i] >= total_lambs:
            break
        i += 1
    Min = len(lst2)-1
    print(lst2)
    return(Max-Min)
        
#print(sumFib(5))
print(solution(10))
#([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])