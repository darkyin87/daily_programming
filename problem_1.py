# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


input = [10, 15, 3, 7]
k = 23

def process_input(input, k):
  """
  - Create an empty set
  - Iterate over items
    - If the item already exists in the set then return True
    - Else, Add the difference between item at that position and the expected sum to the set
  - return False
  """
  new_set = set()

  for item in input:
    if item in new_set:
      return True
    else:
      new_set.add(k - item)

  return False

print process_input(input, k)