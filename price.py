#here compute the minimum price from given list of items
#here you have to select K items and l[J] must be purchased
#return the minimum price to purchase K items given l[J] must be included.


price=0
N,K,J=[int(i) for i in input().split()]

l = [int(i) for i in input().split()][:N]
price=price+l[J-1]
l.remove(l[J-1]
l.sort()
for i in range(0,K-1):
	price=price+l[i]

print(price)
