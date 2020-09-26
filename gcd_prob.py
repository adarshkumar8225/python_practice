# cook your dish here
import math
t=int(input())
for i in range(0,t):
    n=int(input())
    l=[int(i) for i in input().split()][:n]
    I=[]
    for i in range(0,n):
        I.append(i+1)
    for i in range(0,n):
        if(l[i]==I[i]):
            continue
        else:
            for j in range(i,-1,-1):
                if(l[i]==l[j]):
                    if(I[i]>I[j]):
                        gcf=math.gcd(I[i],I[j])
                    else:
                        gcf=math.gcd(I[j],I[i])
                        
                    if(l[i]==gcf):
                        I[i]=l[i]
                        break
                        
    if(I==l):
        print("YES")
    else:
        print("NO")
