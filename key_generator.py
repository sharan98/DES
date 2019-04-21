from Dbox import Dbox
from util import hexToBin
parityDropTable = {
    1: 57, 
    2: 49,
    3: 41,
    4: 33,
    5: 25,
    6: 17,
    7: 9,
    8: 1,
    9: 58,
    10: 50,
    11: 42,
    12: 34,
    13: 26,
    14: 18,
    15: 10,
    16: 2,
    17: 59,
    18: 51,
    19: 43,
    20: 35,
    21: 27,
    22: 19,
    23: 11,
    24: 3,
    25: 60,
    26: 52,
    27: 44,
    28: 36,
    29: 63,
    30: 55,
    31: 47,
    32: 39,
    33: 31,
    34: 23,
    35: 15,
    36: 7,
    37: 62,
    38: 54,
    39: 46,
    40: 38,
    41: 30,
    42: 22,
    43: 14,
    44: 6,
    45: 61,
    46: 53,
    47: 45,
    48: 37,
    49: 29,
    50: 21,
    51: 13,
    52: 5,
    53: 28,
    54: 20,
    55: 12,
    56: 4           
}

compressionTable = {
    1: 14,
    2: 17,
    3: 11,
    4: 24,
    5: 1,
    6: 5,
    7: 3,
    8: 28,
    9: 15,
    10: 6,
    11: 21,
    12: 10,
    13: 23,
    14: 19,
    15: 12,
    16: 4,
    17: 26,
    18: 8,
    19: 16,
    20: 7,
    21: 27,
    22: 20,
    23: 13,
    24: 2,
    25: 41,
    26: 52,
    27: 31,
    28: 37,
    29: 47,
    30: 55,
    31: 30,
    32: 40,
    33: 51,
    34: 45,
    35: 33,
    36: 48,
    37: 44,
    38: 49,
    39: 39,
    40: 56,
    41: 34,
    42: 53,
    43: 46,
    44: 42,
    45: 50,
    46: 36,
    47: 29,
    48: 32
}

K = 'aabb09182736ccdd'
K_b = hexToBin(K)
def Lshift(string):
    f = string[0]
    new_str = string[1:] + f
    return new_str

"""
    keyWithParities: 64 bit binary
    returns list with 16 keys, each of length 48 bits
"""
def key_generator(keyWithParities = K_b):
    keys = []       # list to store the 16 subKeys
    key = Dbox(keyWithParities, parityDropTable)    # 64 bits -> 56 bits : Compression D box
    left = key[:28]
    right = key[28:]
    left_shift = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)
    for round in range(16):
        left = Lshift(left)
        right = Lshift(right)
        if left_shift[round] == 2:
            left = Lshift(left)
            right = Lshift(right)
        k = Dbox(left + right, compressionTable)    # 56 bits -> 48 bits : Compression D box
        keys.append(k)
    return keys
