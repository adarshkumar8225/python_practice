#function call for insertion sort.

def insertion_sort(seq):
    for i in range(1,len(seq)):
        for j in range(0,i):
            if(seq[i]<=seq[j]):
                p=seq[i]
                for k in range(i,j,-1):
                    seq[k]=seq[k-1]
                seq[j]=p
                break
    return(seq)


seq=[2,4,5,1,3,7,5,6,3,78,34,52,12,45,35,23]
#seq=[]
#seq.extend(input())
insertion_sort(seq)
print(seq)

