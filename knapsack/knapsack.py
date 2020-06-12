#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    ind = items[0]
    sz = items[1]
    val = items[2]

    if capacity == 0 or ind == 0:
      return 0

    if (sz[ind-1]) > capacity:
      # return knapsack_solver(capacity, sz, val, ind-1)
      return knapsack_solver(capacity, Item(ind-1, sz, val))
    else:
      return max(
        val[ind-1] + knapsack_solver(capacity-sz[ind-1], Item(ind-1, sz, val)),
          knapsack_solver(capacity, Item(ind-1, sz, val))
        )
    


# # A naive recursive implementation 
# # of 0-1 Knapsack Problem 
  
# # Returns the maximum value that  
# # can be put in a knapsack of  
# # capacity W 
# def knapSack(capacity, weight, value, numofitems): 
  
#     # Base Case 
#     if numofitems == 0 or capacity == 0 : 
#         return 0
  
#     # If weight of the nth item is  
#     # more than Knapsack of capacity W,  
#     # then this item cannot be included  
#     # in the optimal solution 
#     if (weight[numofitems-1] > capacity): 
#         return knapSack(capacity, weight, value, numofitems-1) 
  
#     # return the maximum of two cases: 
#     # (1) nth item included 
#     # (2) not included 
#     else: 
#         return max( 
#             value[numofitems-1] + knapSack( 
#                 capacity-weight[numofitems-1], weight, value, numofitems-1),  
#                 knapSack(capacity, weight, value, numofitems-1)) 
  
# # end of function knapSack 
  
# # To test above function 
# val = [60, 100, 120] 
# wt = [10, 20, 30] 
# W = 50
# n = len(val) 
# print knapSack(W, wt, val, n) 
  
# # This code is contributed by Nikhil Kumar Singh 





if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')