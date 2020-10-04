# cook your dish here
import math
t=int(input())
for i in range(0,t):
    N=int(input())
    A=[int(i) for i in range(1,N+1)]
    B=[int(i) for i in input().split()][:N]
    for i in range(0,N):
        if(A[i]==B[i]):
            continue;
        for j in range(i,-1,-1):
            if(B[i]==B[j]):
                x=math.gcd(A[j],A[i])
                if(x==B[j]):
                    A[i]=x
    if(A==B):
        print("YES")
    else:
        print("NO")
