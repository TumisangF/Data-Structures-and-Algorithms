def containsDuplicates(nums):
  
  # set allows us to check if the element exist in the set, if not we add it to a set
  
  unique_set = set() 
  
  for num in nums:
    if num not in unique_set():
      unique_set.add(num)
    else:
      return true
  return false

# Time  : O(n)
# space : O(n)

# Additional notes
# Sets are implemented hash table. So you can expect a insert/delet/look up of O(1) average.
