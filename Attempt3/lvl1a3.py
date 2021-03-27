#data is a list of ints, n is a postive int
#solution returns the list with ints occuring n times or more removed
#maintians orginal list order
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
def solution(data,n):
    newlst = []
    lst = []
    #data2 = data
    for i in range(0,len(data)):
        if countX(data,data[i]) <= n:
            newlst.append(data[i])
            
    return(newlst)