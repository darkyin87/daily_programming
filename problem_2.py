# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?



input = [1, 2, 3, 4, 5]

[1, 2, 6, 24, 120]


def process(input):
  """
  Product except current element can be stated as the running product of all items before that item + running product of  all items after the item
  in other words for given any element the output is product[0...i-1] * product[i+1...n] which can be done in 2 passes
  """
  product = 1
  counter = 0
  output = []

  for item in input:
    output.append(product)
    product = product * item

  counter = len(input) - 1
  product = 1
  for item in input[::-1]:
    output[counter] = output[counter] * product
    product = product * input[counter]
    counter = counter - 1

  return output
  

print process(input)