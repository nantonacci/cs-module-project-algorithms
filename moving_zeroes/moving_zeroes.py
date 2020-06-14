'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeros = []
    popcount = 0
    n = 0
    zerocount = 0
    arrlength = len(arr)
    print(arrlength)
    for i in arr:
        if i == 0:
            zerocount+=1
            print(zerocount)
        else:
            pass
    
    if zerocount == arrlength:
        pass

    else:
        while n < len(arr)-popcount:
            print(arr)
            if arr[n] != 0:
                print(arr)
                n+=1
            elif arr[n] == 0:
                print(arr)
                zeros.append(arr[n])
                arr.pop(n)
                popcount+=1
                n-=1

    arr+=zeros
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")