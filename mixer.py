from Ebox import Ebox
from whitener import whitener
from Sbox import Sbox, sboxes
from Dbox import Dbox
from util import xor
import itertools

sample_key = '101101101101101101101101101101101101101101101101'
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

"""
    binary_string is the right half of the previous round's output.
    It must be 32 bits long.
    First expanded to 48 bits.
    Then whitened with the 48 bit key.
    Then sent through Sboxes
    Returns 32 bit binaary string
"""
def des_func(binary_string, key = sample_key):
    assert(len(binary_string) == 32), 'Binary string not 32 bits long: {}'.format(len(binary_string))
    expanded = Ebox(binary_string)
    whitened = whitener(expanded, key)
    i = 6
    l = []
    for sbox in itertools.cycle(sboxes):
        if i > 48:
            break
        w= whitened[i - 6: i]
        s = Sbox(w, sbox)
        l.append(s)
        i += 6
    S = ''.join(l)
    P = Dbox(S, Ptable)
    return P

"""
    binary_string must be 64 bits long.
    des_func is applied to right half.
    Then, xor with the left half.
    Returns 64 bits long binary string
"""
def mixer(binary_string, key = sample_key):
    left = binary_string[:32]
    right = binary_string[32:]
    R = des_func(right, key)
    L = xor(left, R)
    L = format(L, '0>32b')
    mixed = L + right
    return mixed