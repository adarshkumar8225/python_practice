#here we have to find two string are anargam or not...... anargam means two string string 
# have same number and type of character.....
# i made two dictionary which keeys type of character as key and number of particular character as its value
#we finally get two dictionary now if both dictionary are equal then print YES else print NO......


t=int(input())
res={}
result={}
for i in range(0,t):
    #to take input two string seperated by spaces in same line
    m,n=map(str,input().split())
    #used to count the frequency of each char in the string1
    for keys in m:
        #if keys are present then get() return the value and 1 is added
        #if keys are not present then key is created and value is added to 1
        res[keys]=res.get(keys,0)+1
    
    #used to count the frequency of each char in string2    
    for key in n:
        result[key]=result.get(key,0)+1
    
    #if both dictionary contains same frequency and same characters
    if(res==result):
        print("YES")
    else :
        print("NO")
        
    res.clear()#clear dictionary for next iteration.
    result.clear()
