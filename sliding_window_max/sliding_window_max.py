'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

#  a[start:stop]  # items start through stop-1

def sliding_window_max(nums, k):
    # Your code here
# window arr of k elements
# slice
# moves one at a time - [1,2,3], [2,3,4], [3,4,5]
# get highest number for each slice - 3, 4, 5
# return arr of highest numbers - [3, 4, 5]
    arrlen = len(nums)
    # increment slice?
    start = 0
    stop = k
    highest = []
    while stop <= arrlen:
        highest.append(max(nums[start:stop]))
        start+=1
        stop+=1
    return highest


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
