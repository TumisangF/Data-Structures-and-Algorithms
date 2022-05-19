def isIsomorphicStrings(s,t):
  mapST,mapTS = {},{}
  
  if len(s) != len(t)
    return false
  
  for i in range(len(s)):
    char1,char2 = s[i],t[i]
    
    # map s[first_char] ---> t[first_char]
    # but first check to see if the don't already exist
    if (char1 in mapST and mapST[char1] != char2) or
       (char2 in mapTS and mapTS[char2] != char1)
      return False
    mapST[char1] = char2
    mapTS[char2] = char1
  
  # Everything checks out
  return true
