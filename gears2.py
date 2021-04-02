def solution(pegs):
    Ls=[]
    for i in range(1,len(pegs)):
        Ls.append(pegs[i]-pegs[i-1]) #generate Ls, L1=a+b, L2=b+c, etc
    #print(Ls)
    rn=0                         #0 + L1
    for i in range(0,len(Ls)):  #Alternate + -
        if i%2==0:
            rn=rn+Ls[i]       #Because we index starting with 0, and L1, L2, L3...Ln are starting at 1, evens and odds are flipped from algebra
        else:
            rn=rn-Ls[i]
    #print(rn)
    if len(Ls)%2==0:  #a-e=L1-L2+L3....
        x=2*rn
    else:                       #x=2.66666=8/3,  right now x=4
        if rn%3!=0:
            xnum=rn*2
            xden=3
        x=(2*rn)/3  #a+e=
    
    #print(x)
    y=rn
    if len(Ls)%2==1:
        y=rn/3

    radii=[x]
    for i in range(0,len(Ls)):  #a=x,   b=L1-x,  c=L2-b
        radii.append(Ls[i]-radii[i])
        if i+1<len(Ls)-1:
            if radii[i+1]>Ls[i+1]:
                return [-1,-1]
    print(radii)
    if x<1 or Ls[0]<x or Ls[-1]<x: #if radius no worky, return [-1,-1]
        return [-1,-1]
    if x%1!=0:
        return [xnum,xden]
    return [int(x),1]
