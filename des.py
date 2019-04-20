from mixer import mixer
from swapper import swapper
from Dbox import Dbox
import itertools

sample_key = '101101101101101101101101101101101101101101101101'
initial_P_table = {
                    1: 58,
                    2: 50,
                    3: 42,
                    4: 34,
                    5: 26,
                    6: 18,
                    7: 10,
                    8: 2,
                    9: 60,
                    10: 52,
                    11: 44,
                    12: 36,
                    13: 28,
                    14: 20,
                    15: 12,
                    16: 04,
                    17: 62,
                    18: 54,
                    19: 46,
                    20: 38,
                    21: 30,
                    22: 22,
                    23: 14,
                    24: 6,
                    25: 64,
                    26: 56,
                    27: 48,
                    28: 40,
                    29: 32,
                    30: 24,
                    31: 16,
                    32: 8,
                    33: 57,
                    34: 49,
                    35: 41,
                    36; 33,
                    37: 25,
                    38: 17,
                    39: 9,
                    40: 1,
                    41: 59,
                    42: 51,
                    43: 43,
                    44: 35,
                    45: 27,
                    46: 19,
                    47: 11,
                    48: 3,
                    49: 61,
                    50: 53,
                    51: 45,
                    52: 37,
                    53: 29,
                    54: 21,
                    55: 13,
                    56: 5,
                    57: 63,
                    58: 55,
                    59: 47,
                    60: 39,
                    61: 31,
                    62: 23,
                    63: 15,
                    64: 7,
                
            
}


final_P_table= {
                    1: 40,
                    2: 8,
                    3: 48,
                    4: 16,
                    5: 56,
                    6: 24,
                    7: 64,
                    8: 32,
                    9: 39,
                    10: 7,
                    11: 47,
                    12: 15,
                    13: 55,
                    14: 23,
                    15: 63,
                    16: 31,
                    17: 38,
                    18: 6,
                    19: 46,
                    20: 14,
                    21: 54,
                    22: 22,
                    23: 62,
                    24: 30,
                    25: 37,
                    26: 5,
                    27: 45,
                    28: 13,
                    29: 53,
                    30: 21,
                    31: 61,
                    32: 29,
                    33: 36,
                    34: 4,
                    35: 44,
                    36; 12,
                    37: 52,
                    38: 20,
                    39: 60,
                    40: 28,
                    41: 35,
                    42: 3, 
                    43: 43,
                    44: 11,
                    45: 51,
                    46: 19,
                    47: 59,
                    48: 27,
                    49: 34,
                    50: 2,
                    51: 42,
                    52: 10,
                    53: 50,
                    54: 18,
                    55: 58,
                    56: 26,
                    57: 33,
                    58: 1,
                    59: 41,
                    60: 9,
                    61: 49,
                    62: 17,
                    63: 57,
                    64: 25,
                
            
}
"""
    binary_string must be 64 bits long.
    key must be 48 bits long.
    Returns 64 bits long binary string.
"""
# def des_round(binary_string, key = sample_key):
#     mixed = mixer(binary_string, key)
#     swapped = swapper(mixed)
#     return swapped
"""
    binary_string must be 64 bits long.
    key must be 48 bits long.
    Returns 64 bits long binary string.
"""
def encryptBlock(binary_string, keys = [sample_key]):
    init_permuted = Dbox(binary_string, initial_P_table)
    b = init_permuted
    for r in range(16):
        b = mixer(b, keys[0])
        if r != 15:
            b = swapper(b)
    fin_permuted = Dbox(binary_string, final_P_table)
    return fin_permuted

def decryptBlock(binary_string, keys = [sample_key]):
    init_permuted = Dbox(binary_string, initial_P_table)
    b = init_permuted
    for r in range(16):
        b = mixer(b, keys[0])
        if r != 15:
            b = swapper(b)
    fin_permuted = Dbox(binary_string, final_P_table)
    return fin_permuted
