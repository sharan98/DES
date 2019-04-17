sbox = {
    '00': [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    '01': [0, 15, 7, 4, 14, 2, 13, 10, 3, 6, 12, 11, 9, 5, 3, 8],
    '10': [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    '11': [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 13, 14, 10, 0, 6, 13]
}

"""
    binary_string must be 6 bits long.
    First and last bits together form the row.
    remaining bits form the coloumn.
    returns 4 bit string
"""
def Sbox(binary_string, sbox = sbox):
    row = binary_string[0] + binary_string[5]
    col = int(binary_string[1:5], 2)
    sub = sbox[row][col]
    return format(sub, '0>4b')
