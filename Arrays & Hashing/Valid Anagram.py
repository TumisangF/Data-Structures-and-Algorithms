'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

'''

### Brute force solution
### Sort each char in both strings and compare them

s,t = "anagram", "nagaram"
s2,t2 = 'rat','car'


def validAnagram(s,t):

    # Test case 1: lengths have to be the same
    if len(s) != len(t):
        return False

    # sorted list of S and T
    s_list = sorted(s) # s_list = ['a', 'a', 'a', 'g', 'm', 'n', 'r']
    t_list = sorted(t) # t_list =  ['a', 'a', 'a', 'g', 'm', 'n', 'r']

    # compare each char for each string
    for i in range(len(s_list)):
        if s_list[i] != t_list[i]:
            return False
    return True

#print(validAnagram(s2,t2))

'''
Time: O(nlogn) >> sort() is using  Timesort Algorithm
Space: O(n) >> O(2*n) 
'''

#*****************************************************************************************************************
#*****************************************************************************************************************
#*****************************************************************************************************************

# Opitmal solution
# Create two dictionaries for each string
# Use chars as keys, frequency as values
# Compare frequencies for each char in two dictionaries


def validAnagram2(s,t):
    s_dict,t_dict = {},{}
    
    for i in range(len(s)):
        s_dict[s[i]] = s_dict.get(s[i],0) + 1
        t_dict[t[i]] = t_dict.get(t[i],0) + 1

    for j in s:
        if s_dict[j] != t_dict.get(j,0):
            return False
    return True

print(validAnagram2(s2,t2))


'''
Time: O(n) << O(2*n)
Space: O(n) << O(2*n) 
'''

### One line of code

def validAnagram3(s,t):
    return sorted(s) == sorted(t)