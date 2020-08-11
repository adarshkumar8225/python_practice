# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(0,T):
    n=int(input())
    l = [int(i) for i in input().split()][:n]
    #print(l)
    #for i in range(0,n):
    #    e=int(input())
    #   l.append(e)

    s=l[:]
    flag1=0
    flag2=0
    #start from leftmost element.
    while(len(s)>1):
        x=s[0]
        del s[0]
        if(x<s[0] and x<s[-1]):
            flag1=1
            break
        elif(x>= s[0]):
            del s[0]
        elif(x>=s[-1]):
            del s[-1]
   # if(len(s)==2 and flag1==0):
   #    x=s[0]
   #     del s[0]
    #    if(x<s[0]):
    #        flag1=1
    #    del s[0]
    while(len(l)>1):
        x=l[-1]
        del l[-1]
        if(x<l[0] and x<l[-1]):
            flag2=1
            break
        elif(x>= l[0]):
            del l[0]
        elif(x>=l[-1]):
         del l[-1]
    #if(len(l)==2 and flag2==0):
    #    x=l[0]
    #    del l[0]
    #    if(x<l[0]):
    #        flag2=1
    #    del l[0]
    if(flag1==1 and flag2==1):
        print('Yes')
    else :
        print('No')
     
    
