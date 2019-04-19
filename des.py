from mixer import mixer
from swapper import swapper
from Dbox import Dbox
import itertools

sample_key = '101101101101101101101101101101101101101101101101'

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
