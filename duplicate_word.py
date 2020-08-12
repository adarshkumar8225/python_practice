# count the no. of duplicates word and print the count.



n=int(input())
l=[]
for i in range(0,n):
    word=input()
    l.append(word)
my_dict = {i:l.count(i) for i in l}
key=my_dict.keys()
distinct=len(key)
print(distinct)
for i in key:
    print(my_dict[i],end=' ')
