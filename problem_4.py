# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

input = [3, 4, -1, 1]
# input = [1, 2, 0]

def process(input):
  """
  - Sort the list this could be done in O(nlogn)
  - Traverse the sorted list and find the first missing positive integer O(n)
  """
  input = sorted(input)

  for idx, item in enumerate(input):
    if item > -1 and len(input) > idx+1:
      if input[idx+1] != item + 1:
        return item + 1
  
  if item + 1 > 0:
    return item + 1
  else:
    return 1


print process(input)