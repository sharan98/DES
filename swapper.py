""" 
    Swaps the left and right halves of binary string
    Binary string length must be even
"""
def swapper(binary_string):
    size = len(binary_string)
    assert (size % 2 == 0), 'Binary string length is not even'
    mid_index = size // 2
    left = binary_string[:mid_index]
    right = binary_string[mid_index:]
    return right + left