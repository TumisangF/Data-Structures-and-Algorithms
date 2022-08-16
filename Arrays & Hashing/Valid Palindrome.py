'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

def validAnagram(s):

    string = ''

    for char in s:
        if char.isalnum() == True:
            string += char
    
    return string.lower() == string[::-1].lower()

# Time: O(n)
# Space: O(n)