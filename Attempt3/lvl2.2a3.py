from fractions import Fraction as frac
def solution(pegs):
    dist = (pegs[-1])-(pegs[0])
    #print(dist)
    l1 = pegs[1]-pegs[0]
    for m in range(1,l1-1,1):
        a = dist-m
        if (l1-m)/2+l1 == a:
            val = l1-m
            if type(val) == int:
                return [val,1]
            s = str(val)
            f = frac(s)
            print(f)
            #s2 = str(f)
            #return s2       
    return[-1,-1]
    
print(solution([4,30,50]))
print(solution([1,16,37]))