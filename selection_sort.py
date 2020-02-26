def selection_sort(seq):
    for i in range(len(seq)):
        min=seq[i]
        for j in range(i,len(seq)):
            if(seq[j]<=min):
                min=seq[j]
                min_pos=j
        (seq[i],seq[min_pos])=(seq[min_pos],seq[i])
    return(seq)


#seq=[2,5,7,1,9,6]
seq=[]
#n=int(input("enter the no. of elements"))
#for i in range(n):
seq.extend(input())

selection_sort(seq)
print(seq)

