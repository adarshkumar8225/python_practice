# cook your dish here
t=int(input())
for i in range(0,t):
    N=int(input())
    count=0
    A=[int(i) for i in range(1,N+1)]
    B=[int(i) for i in input().split()][:N]
    for i in range(0,N):
        if((A[i]%B[i])!=0):
            print("NO");
            break;
        else:
            count=count+1
    if(count==N):
        print("YES")
