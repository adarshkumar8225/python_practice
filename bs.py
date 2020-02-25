def binary_search(seq,v,left,right):
    if(right==left):
        return(0)
    mid=(left + right)//2

    if(seq[mid]== v):
        return(1)
    elif(seq[mid] > v):
        return(binary_search(seq,v,left,mid))
    else:
        return(binary_search(seq,v,mid+1,right))
    


seq=[2,5,6,8,9,12,19,43]
v=1

left=0
right=len(seq)
p=binary_search(seq,v,left,right)
print(p)

