#print the number triangle:
#1
#22
#333
#...
#using only one print statement.



for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i)//9 *i)
