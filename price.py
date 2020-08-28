price=0
N,K,J=[int(i) for i in input().split()]

l = [int(i) for i in input().split()][:N]
price=price+l[J-1]
l.sort()
for i in range(0,K-1):
	price=price+l[i]

print(price)
