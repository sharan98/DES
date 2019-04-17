"""
    Bitwise xor with 48 bit key
"""
def whitener(binary_string, key, size = 48):
    b = int(binary_string, 2)
    k = int(key, 2)
    res = b ^ k
    spec = '0>{}b'.format(size)
    return format(res, spec)
    