def solution(pegs):
    a=helper(pegs)
    l1=pegs[1]-pegs[0]
    if a>l1:
        return [-1,-1]
    else:
        return [2*a,1]
    
def helper(pegs):
    #print('pegs', pegs)
    if len(pegs)>1:   
        lst = []
        for i in range(1,len(pegs)):
            val = pegs[i-1]-pegs[i]
            if val < 1:
                val = val*-1
            lst.append(val)
        #print('lst', lst)
        x=helper(lst)
    else:
        x=pegs[0]
    return x
