ef solution(pegs):
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
    if len(Ls)%2==0:
        x=2*rn
    else:
        x=(2*rn)/3
    if rn<0 or Ls[0]<x:
        return [-1,-1]
    # x=x.as_integer_ratio()
    # out=[x[0],x[1]]
    return fractioner(x)

def fractioner(x):
    counter=1
    while x%1!=0:
        counter*=10
        x*=10
    tuplx=(x,counter)
    #print(tuplx)
    gcd=gcder(tuplx)
    return [int(tuplx[0]/gcd),int(tuplx[1]/gcd)]

def gcder(tuplx):
    x=tuplx[0]
    y=tuplx[1]
    small=min(x,y)
    gcd=-1
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
