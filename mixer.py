from Sbox import Sbox, sboxes
from Dbox import Dbox
from util import xor, binToHex, hexToBin
import logging

Ptable = {
    1: 16,
    2: 7,
    3: 20,
    4: 21,
    5: 29,
    6: 12,
    7: 28,
    8: 17,
    9: 1,
    10: 15,
    11: 23,
    12: 26,
    13: 5,
    14: 18,
    15: 31,
    16: 10,
    17: 2,
    18: 8,
    19: 24,
    20: 14,
    21: 32,
    22: 27,
    23: 3,
    24: 9,
    25: 19,
    26: 13,
    27: 30,
    28: 6,
    29: 22,
    30: 11,
    31: 4,
    32: 25
}

Etable = {
    1: 32,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 4,
    8: 5,
    9: 6,
    10: 7,
    11: 8,
    12: 9,
    13: 8,
    14: 9,
    15: 10,
    16: 11,
    17: 12,
    18: 13,
    19: 12,
    20: 13,
    21: 14,
    22: 15,
    23: 16,
    24: 17,
    25: 16,
    26: 17,
    27: 18,
    28: 19,
    29: 20,
    30: 21,
    31: 20,
    32: 21,
    33: 22,
    34: 23,
    35: 24,
    36: 25,
    37: 24,
    38: 25,
    39: 26,
    40: 27,
    41: 28,
    42: 29,
    43: 28,
    44: 29,
    45: 30,
    46: 31,
    47: 32,
    48: 1
}

"""
    Bitwise xor with 48 bit key
"""
def whitener(binary_string, key, size = 48):
    res = xor(binary_string, key)
    spec = '0>{}b'.format(size)
    return format(res, spec)

"""
    binary_string is the right half of the previous round's output.
    It must be 32 bits long.
    First expanded to 48 bits.
    Then whitened with the 48 bit key.
    Then sent through Sboxes
    Returns 32 bit binary string
"""
def des_func(binary_string, key):
    assert(len(binary_string) == 32), 'Binary string not 32 bits long: {}'.format(len(binary_string))
    logging.info ("des_func({}, {})".format(binToHex(binary_string), key))

    # Expand from 32 bits -> 48 bits
    expanded = Dbox(binary_string, Etable)
    logging.info ("After expanding: {}".format(binToHex(expanded)))

    # xor with key
    whitened = whitener(expanded, key)
    logging.info ("After whitening: {}".format(binToHex(whitened)))
    i = 6
    l = []
    count = 1

    # Sboxes in chunks of 6 bits
    for s in range(8):
        sbox = sboxes[s]
        w = whitened[i - 6: i]
        s = Sbox(w, sbox)
        logging.info ("Sbox{}, input: {}, output: {}".format(count, w, s))
        l.append(s)
        i += 6
        count += 1
    S = ''.join(l)
    logging.info ('After Sboxes: {}'.format(binToHex(S)))

    # final straight D box
    P = Dbox(S, Ptable)
    logging.info('After final dbox: returning {}'.format(binToHex(P)))
    return P

"""
    binary_string must be 64 bits long.
    key must be 48 bits long.
    des_func is applied to right half.
    Then, xor with the left half.
    Returns 64 bits long binary string
"""
def mixer(binary_string, key):
    assert (len(binary_string) == 64), "Binary string is not 64 bits long: {}".format(len(binary_string))
    assert (len(key) == 48), "Binary string is not 48 bits long: {}".format(len(key))
    logging.info ("Mixing: {}".format(binToHex(binary_string)))
    left = binary_string[:32]
    right = binary_string[32:]
    R = des_func(right, key)
    L = xor(left, R)
    L = format(L, '0>32b')
    logging.info ('returning - left: {}, right: {}'.format(L, right))
    mixed = L + right
    return mixed