# Map each character to each word
# for the second ocurance of each char and the char does't match the word that it was already mapped to, return False

# e.g pattern = 'abba' ,string = 'dog cat cat dog'

def wordPattern(pattern,string)
	# edge case: if all words in str are the same. creating two dictionaries would solve that.
	# 'abba' and s = 'dog dog dog dog'
	# first iter: a --> dog, dog --> a
	# sec   iter: b --> dog, dog --> b, it would retunr false since same word can't be mapped to two diff characters
        	
	mapCharWord,mapWordChar = {},{}
        
	# create a list of words from the str
	list_words = s.split()
        
	# Lengths have to be the same
	if len(pattern) != len(list_words):
		return False
        
	for i in range(len(pattern)):
		char,word= pattern[i],list_words[i]
          
	# check if there is a occurance of char and word
	if (char in mapCharWord and mapCharWord[char] != word) or (word in mapWordChar and mapWordChar[word] != char):
		return False
            
		mapCharWord[char] = word
		mapWordChar[word] = char
       
	# Everything checks out
	return True
    
	
  
