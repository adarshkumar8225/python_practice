# count the no. of duplicates word and print the count.
dict={}
#loop for taking the input words.
for i in range(int(input())):
    #If input not in the dictionary, then add it
    #else increment the counter
    key = input()
    if not key in dict.keys(): #keys() returns keys used in the dictionary.
        dict.update({key : 1})
        continue
    dict[key] += 1

print(len(dict.keys()))
print(*dict.values())

