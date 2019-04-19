from util import xor
"""
    Bitwise xor with 48 bit key
"""
def whitener(binary_string, key, size = 48):
    res = xor(binary_string, key)
    spec = '0>{}b'.format(size)
    return format(res, spec)