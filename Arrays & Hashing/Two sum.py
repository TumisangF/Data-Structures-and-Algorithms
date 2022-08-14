'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''

# Brute force solution
# Take each num and look all other number to see if they add up to k


nums,k = [2,7,11,15], 9
nums2,target = [3,2,4], 6

def twoSum(nums,k):
    for i,num in enumerate(nums):
        for j in range(i+1,len(nums)):
            if num + nums[j] == k:
                return [i,j]

print(f'Brute force solution output: {twoSum(nums2,target)}')

'''
Time: O(n^2)
Space: O(1)
'''

#*****************************************************************************************************************
#*****************************************************************************************************************
#*****************************************************************************************************************

# Optimal Solution


def twoSum2(nums,k):
    
    dict = {}

    for i,num in enumerate(nums):
        diff = k - num
        if diff not in dict:
            dict[num] = i
        elif diff in dict:
            return [i,dict[diff]]

print(f'Optimal solution output: {twoSum2(nums2,target)}')