#return the maximum prod on a list of integers
def solution4(xs):
    if len(xs) == 2:
        prod = xs[0]*xs[1]
        return str(prod)    
    if len(xs) == 1:
        return str(xs[0])
    low = 0
    count = 0
    prod = 1
    for i in range(1,len(xs)+1):
        if xs[i-1] != 0:
            #print(xs)
            prod = prod * xs[i-1]
            #############
            if xs[i-1] < 0:
                if low == 0:
                    low = xs[i-1]
                elif xs[i-1] > low:
                    low = xs[i-1]
            else:
                low = low
            #############
                
        else:
            count = count + 1
            if count == len(xs):
                return str(0)       
    
    if prod < 0 and low != 0 and count < len(xs)-1:
        prod = prod//low
    else:
        if prod < 0:
            prod = 0 
        else:
            prod = prod
        
    return(str(prod))
            
print(solution4([0,-1,0]))