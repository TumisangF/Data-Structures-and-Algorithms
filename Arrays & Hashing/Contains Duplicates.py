'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# Brute force solution
# Take each num and compare it with the rest
# >> 1 compare it with [2,3,1]
# >> 2 compare it with [3,1]

nums = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

def firstSolution(nums):
    for i,num in enumerate(nums):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

#print(firstSolution(nums3))

'''
Time: O(n^2)
Space: O(1)
'''
#*****************************************************************************************************************
#*****************************************************************************************************************
#*****************************************************************************************************************

# 2nd Solution
# use set data structure
# set() does not allow for duplicates
# set() is implemented as a hash table>> lookup/insert/delet of O(1)

def secSolution(nums):
    nums_set = set()
    for num in nums:
        if num not in nums_set:
            nums_set.add(num)
        elif num in nums_set:
            return True
    return False

'''
Time: O(n)  >> You could potentially scan every element but Once
Space: O(n) >> You could potentially add every element in the set()
'''


#print(secSolution(nums3))


def containsDuplicate(nums):
    return len(nums) != len(set(nums))

print(containsDuplicate(nums3))