'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

## Brute force solution
## Sort the characters in each word



### Optimal solution
from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)

    for str in strs:
        count = [0] * 26 # 26 0s. One 0 for each character

        for char in str:
            count[ord(char) - ord('a')] += 1 # The ord() function returns the number representing the unicode code of a specified character.
        
        res[tuple(count)].append(str)
    
    return res.values()
