'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''
nums = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]

# Optimal solution

def sequence(nums):

    nums_set = set(nums) # A set has a lookup/insert/delete of a costant time because it is implemeted as a hashtable.
    output = 0

    for num in nums:

        # check if the num is the first in its sequence
        if (num - 1) not in nums_set:
            length = 1
            while (num + length) in nums_set:
                length += 1
            output = max(output, length)
    
    return output

print(f'Optimal solution output: {sequence(nums2)}')

# Time: O(n)
# Space: 0(n)

