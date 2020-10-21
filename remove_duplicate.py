	#keep only first occurance of string ex: geeksforgeeks will give geksfor
  #use dictionary and first occurance of a char will be the key .
  #if again some character occurs the delete that character.......
  def removeDups(self, S):
	
        #code here
	dict1={}
	M=""
	for keys in S:
		#if the character occured first time then add it to string M
		if(keys not in dict1.keys()):
			dict1[keys]=dict1.get(keys,0)+1
		        M=M+keys

	return M

