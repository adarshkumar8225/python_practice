# cook your dish here
t=int(input())
for i in range(0,t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    count=0
    leftover=0
    ans=0
    for i in range(0,n):
        count=l[i]+count
        #leftover=count-k
        if(count<k):
            ans=i+1
            break
        count=count-k
    if(count>k):
        ans=n+(count//k)+1
    print(ans)
