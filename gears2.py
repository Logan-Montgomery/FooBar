def solution(pegs):
    Ls=[]
    for i in range(1,len(pegs)):
        Ls.append(pegs[i]-pegs[i-1]) #generate Ls
    print(Ls)
    rn=Ls[0]
    for i in range(1,len(pegs)-1):
        if i%2==0:
            rn=rn+Ls[i]
        else:
            rn=rn-Ls[i]
    print(rn)
    if len(Ls)%2==0:  #a-e=rn
        x=2*rn
    else:
        x=(2*rn)/3  #a+e=rn
    # y=rn
    # if len(Ls)%2==1:
    #     y=rn/3
    print(x)
    if rn<0 or Ls[0]<rn or Ls[-1]<rn: #if radius no worky, return [-1,-1]
        return [-1,-1]
    if type(x)==float:
        return [int(x*3),3]
    return [x,1]
