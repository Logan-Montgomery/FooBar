def solution(pegs):
    Ls=[]
    for i in range(1,len(pegs)):
        Ls.append(pegs[i]-pegs[i-1])
    #print(Ls)
    rn=Ls[0]
    for i in range(1,len(pegs)-1):
        if i%2==0:
            rn=rn+Ls[i]
        else:
            rn=rn-Ls[i]
    #print(rn)
    if rn<0:
        return [-1,-1]
    if len(Ls)%2==0:
        x=2*rn
    else:
        x=(2*rn)/3
    x=rn.as_integer_ratio()
    out=[x[0],x[1]]
    return out
