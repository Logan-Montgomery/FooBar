###LEVEL 2### 
# this was the salute problem,
# super easy people '<' walk twards eachother have to salute,
# count the number of salutes needed in a given path
# example --<---<--->--<--
# return 2 salutes, bc 2 people salute 1 time each

def solution(s):
    for i in range(0,len(s)):
        if s[i] == '>':
            for j in range(0,len(s)-i):
                if s[j] == '<':
                    count += 1