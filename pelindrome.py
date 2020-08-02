#input the value of n. then print n lines of pelindrome using only one print statement.
#sample: for n=4 pelindrome with only one print statement.
#1
#121
#12321
#1234321



j=0
for i in range(1,int(input())+1):
     #More than 2 lines will result in 0 score. Do not leave a blank line also
    
    k=1
    m=1

    while(k<=i+j):
        if(k==i+j):
            l='\n'
        else:

            l='' 
        if(k>i):
            m=m-1
        
        print(m,end=l),
        
        if(k<i):
            m=m+1
        k=k+1
    j=j+1
    

