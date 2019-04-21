""" 
    Convert string to hexadecimal 
    each character -> hexadecimal value
"""
def toHex(s, enc = 'utf'):
    # s = ''.join(s.split())
    P = s.encode(enc).hex()
    return P

""" 
    Convert hexadecimal to string
    Opposite of toHex()
"""
def toStr(h, enc = 'utf'):
    P = bytes.fromhex(h).decode(enc)
    return P

""" Convert string to array of 8 bit binaries """
def toBinArray(s, enc = 'utf'):
    s = ''.join(s.split())
    byte_array = bytearray(s, enc)
    bin_array = [format(i, '0>8b') for i in byte_array]
    return bin_array

""" Convert binary array to hexadecimal array """
def toHexArray(bin_array):
    ints = [int(i, 2) for i in bin_array]
    hex_array = [format(i, 'x') for i in ints]
    return hex_array

""" Convert binary array to string """
def binArrayToStr(bin_array):
    hex_array = toHexArray(bin_array)
    hex_str = ''.join(hex_array)
    text = toStr(hex_str)
    return text

""" Convert string to binary """
def strToBin(s, enc = 'utf'):
    s = ''.join(s.split())
    bin_array = toBinArray(s, enc)
    bin_str = ''.join(bin_array)
    return bin_str

""" Convert binary to string """
def binStrToStr(bin_str):
    ar = []
    for i in range(0, len(bin_str), 8):
        ar.append(bin_str[i:i+8])
    text = binArrayToStr(ar)
    return text

"""
    A xor B
    returns an integer
"""
def xor(A, B):
    size = len(A)
    assert (len(B) == size), 'operands not of same size in xor: a = {}, b = {}'.format(A, B)
    a = int(A, 2)
    b = int(B, 2)
    res = a ^ b
    return res

"""
    Convert hexadecimal string to binary string
"""
def hexToBin(hex_string):
    l = []
    for h in hex_string:
        i = int(h, 16)
        l.append(format(i, '0>4b'))
    return ''.join(l)

def binToHex(bin_string):
    i = int(bin_string, 2)
    return format(i, 'x')