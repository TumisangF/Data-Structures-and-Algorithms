def isAnagram(s,t):
  # 1. Lengths have to be the same
  # 2. Create two dictionaries
       # store each character in a dictionary as a key and its frequency as value for all characters in the word 's'
       # store each character in a dictionary as a key and its frequency as value for all characters in the world 't'.
  # 3. Compare the counts for each character 
  # 4. return true if all checks out.
  
  # 1. lengths have to be the same
  if len(s) != len(t):
    return false
  
  # 2. create two dictionaries
  dic_1,dic_2 = {},{}
  
  for i in range(len(s)):
    dic_1[s[i]] = 1 + dic_1.get(s[i],0)
    dic_2[t[i]] = 1 + dic_2.get(t[i],0)
  
  # 3. Compare the counts for each character
  for c in dic_1:
    if dic_1[c] != dic_2[c].get(dic_2[c],0):
      return false
  #if erthang checks out
  return true

# Time:  O(s + t)
# Space: O(s+ t)


# Second solution

from collections import Counter

def isAnagram(s,t):  
  return Counter(s) == Counter(t)
