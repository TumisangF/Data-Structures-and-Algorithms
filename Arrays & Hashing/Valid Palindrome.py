'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

def validAnagram(s):

    string = ''

    for char in s:
        if char.isalnum():
            string += char
    
    return string.lower() == string[::-1].lower()

# Time: O(n)
# Space: O(n)


# Two pointer approach

def validAnagram2(s):

    # initialize the left and right poiter
    l,r = 0, len(s)-1

    # As long as left and right pointer don't meet.
    while l < r:
        # first check if the current elements on both sides are alphnumeric
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() == s[r].lower():
                l +=1
                r -=1
            elif s[l].lower() != s[r].lower():
                return False
        # if either of the characters on both sides are not alphanumeric
        elif not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
    
    return True

s = "A man, a plan, a canal: Panama"
print(validAnagram2(s))
        
# Time: O(n)
# Space: O(1)

# If you don't want to use the builtin isalnum() method

def alnum(self,char):
    return (ord('A') <= ord(char) <= ord('Z')) or (ord('a') <= ord(char) <= ord('z')) or (ord(0) <= ord(char) <= ord(9))
    