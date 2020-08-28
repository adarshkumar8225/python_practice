string=input()
sum=0
for i in range(0,len(string)):
	for j in range(i+1,len(string)):
		if(string[i]==string[j]):
			sum=sum+(j-i)
print(sum)
