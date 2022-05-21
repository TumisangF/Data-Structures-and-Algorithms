# Map each character to each word
# for the second ocurance of each char and the char does't match the word that it was already mapped to, return False

# e.g pattern = 'abba' ,string = 'dog cat cat dog'

def wordPattern(pattern,string)
  # mapPS char --> word
  # mapSP word --> char
  mapPS,mapSP = {},{}
  
  # create a a list of words from the string
  list_words = string.split()
  
  # The lengths should be the same
  if len(pattern) != len(string):
    return False
  
  for i in range(len(pattern)):
    char,word = pattern[i],list_words[i]
    
    #if there is a mapping already of char/word
    if (char in mapPS and mapPS[char] != word) or (word in mapSP and maSP[word] != char):
      return False
    
    mapPS[char] = word
    mapSO[word] = word
    
  # if everything checks out
  return True
    
  
