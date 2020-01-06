# calculate the hamming distance between two numbers
# count the number of 1 after xor operation of two number
#  citation: https://leetcode.com/articles/hamming-distance/

# approach 1: using library function
def hamming_distance_using_library(x, y):
    xor = x ^ y
    return bin(xor).count('1')


# approach 2: using bit shifting

def hamming_distance_bit_shift(x, y):
    xor = x ^ y
    distance = 0
    while xor:
        if xor & 1:
            # found 1
            distance = distance + 1
        xor = xor >> 1
    return distance


# approach 3: Brian Kernighan's Algorithm
# approach 3 is faster than apporach 2
def hamming_distance_brian_kernighan(x, y):
    xor = x ^ y
    distance = 0
    while xor:
        xor = xor & (xor - 1)  # clears the right most set bit
        distance = distance + 1
    return distance
