	#keep only first occurance of string ex: geeksforgeeks will give geksfor
  #use dictionary and first occurance of a char will be the key .
  #if again some character occurs the delete that character.......
  
  def removeDups(self, S):
	     #code here
		dict1={}
		i=0
		for keys in S:
		    
		    if(keys in dict1.keys()):
		        S=S[:i]+S[i+1:]#deleting a char from S so i is not incremented.
		        
		    else:
		        dict1[keys]=dict1.get(keys,0)+1
		        i=i+1
		return S
