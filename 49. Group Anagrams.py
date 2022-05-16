# e.g [["eat","tea","tan","ate","nat","bat"]]

def groupAnagrams(strings):
  
  dictionary = {} # Mapping charCount ---> list Of Anagrams
  
  # Go through every string
	# e.g 'eat'
	for string in strings:
		count = [0] * 26 # 26 zeros..One for each character...a --- z
		
		# Go through every single character in the string. e.g 'eat'
		# e.g 'e'
		for char in string:
			count[ord(char)-ord('a')] += 1
		
		dictionary[tuple(count)].append(string) # lists can not be key in Python
	
	return dictionary.values()
