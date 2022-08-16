'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''

# We can't use a hashmap because we have a restriction of using only a constant extra space
# Use Two poiters approach

'''
1 + 11 = 12: > target so >> move the right poiter since they are sorted
1 + 10 = 11: > target so >> move the right poiter again
1 + 7 = 8: < target so >> move the left pointer
3 + 7 = 10: > tagert so >> move the right pointer
3 + 5 = 8: < target so >> move the left pointer
4 + 5 = 9 = target: return l+1, r+1 since one-indexed

Conditions:
> Move the right poiter if sum > target
> Move the left poiter if sume < target
> return [l+1,r+1]
'''



def twoSumII(numbers,target):
    l,r = 0, len(numbers) - 1

    while l < r:
        sum = numbers[l] + numbers[r]

        if sum == target:
            return [l+1,r+1]
        elif sum > target:
            r -= 1
        elif sum < target:
            l += 1
    

numbers  = [1,3,4,5,7,10,11]
target = 9
print(f'Optimal solution outcome: {twoSumII(numbers, target)}')

# Time: O(n)
# Space: O(1)