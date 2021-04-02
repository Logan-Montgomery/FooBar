def solution(pegs):
    Ls=[]
    for i in range(1,len(pegs)):
        Ls.append(pegs[i]-pegs[i-1])
    print(Ls)
    rn=Ls[0]
    for i in range(1,len(pegs)-1):
        if i%2==0:
            rn=rn+Ls[i]
        else:
            rn=rn-Ls[i]
    print(rn)
    if len(Ls)%2==0:
        out=[2*rn,1]
    else:
        out=[(2*rn)/3.0,1]
    return out
