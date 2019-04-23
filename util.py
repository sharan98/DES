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

""" Convert byte array to binary string """
def bytesToBinString(byte_array):
    bin_array = [format(i, '0>8b') for i in byte_array]
    return ''.join(bin_array)

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
    A and B are both binary strings
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
    Each hex digit -> 4 bit binary
    Eg: '02' -> '00000010'
"""
def hexToBin(hex_string):
    l = []
    for h in hex_string:
        i = int(h, 16)
        l.append(format(i, '0>4b'))
    return ''.join(l)

"""
    binary string to hexadecimal.
    First grouped to bloxks of 4bits.
    Eg: '00000010' -> '02'
"""
def binToHex(bin_string):
    l = []
    for i in range(0, len(bin_string), 4):
        b = bin_string[i: i + 4]
        i = int(b, 2)
        l.append(format(i, '0>1x'))
    return ''.join(l)