def twoSum(nums):
  hashMap = {} # {value: index}
  
  for index,element in enumerate(nums):
    diff = target - element
    
    if diff in hashMap:
      return [hashMap[diff],index]
    hashMap[element] = index
    
# Time Complexity: O(n)   ... Run through the array only once
# Space Complextiy: O(n)  ... Because of the dictionary I created
    
