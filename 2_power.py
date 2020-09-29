# Hello World program in Python
n=int(input())
l=[int(i) for i in input().split()][:n]
k=l[:]
print(k)
count=0
summation=0
for i in range(0,n):
    if(l[i]==1):
        count=count+1
        summation=summation+l[i]
        continue
    while(k[i]>1):
        rem=k[i]%2
        k[i]=k[i]/2
        print("hello")
        if(rem!=0):
            break
    if( rem==0):
        count=count+1
        summation=summation+l[i]
    
print(count)
print(summation)
