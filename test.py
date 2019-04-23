from util import toHex, toStr, binToHex, hexToBin, bytesToBinString
from des import encryptBlock, decryptBlock

"""
    p_x: hex string - 64 bits long
    KEY: hex string - 64 bits long
    returns cipher text as a hex string
"""
def encryptHex(p_x, KEY):
    KEY_b = hexToBin(KEY)
    assert (len(KEY_b) == 64), 'KEY is not the correct size: encryptString'
    assert (len(p_x) == 16), 'hex plaintext not long enough'
    p_b = hexToBin(p_x)
    c_b = encryptBlock(p_b, KEY_b)
    c_x = binToHex(c_b)
    return c_x

"""
    c_x: hex string - 64 bits long
    KEY: hex string - 64 bits long
    returns plain text as a hex string
"""
def decryptHex(c_x, KEY):
    KEY_b = hexToBin(KEY)
    assert (len(KEY_b) == 64), 'KEY is not the correct size: encryptString'
    assert (len(c_x) == 16), 'hex plaintext not long enough'
    c_b = hexToBin(c_x)
    d_b = decryptBlock(c_b, KEY_b)
    d_x = binToHex(d_b)
    return d_x
"""
    P: plaintext string. Eg: 'hello'
    KEY: hexadecimal string - 64 bits
    Eg KEY = 'aabb09182736ccdd'
    This is a generator: yields ciphertext of 64 bit blocks.
"""
def encryptStringToHex(P, KEY):
    assert (len(KEY) == 16), 'KEY is not the correct size: encryptString'
    extra = 8 - len(P) % 8
    if extra % 8 != 0:
        P = P + ' ' * (extra)
    l = []
    for i in range(0, len(P), 8):
        p = P[i: i + 8]

        P_x = toHex(p)
        C_x = encryptHex(P_x, KEY)
        # yield (C_x)
        l.append(C_x)
    return ''.join(l)

"""
    C_x: ciphertext hexa string. Eg - '26764ff37a99915f'
    KEY: hexadecimal string - 64 bits
    This is a generator: yields plaintext of 64 bit blocks.
"""
def decryptHexToString(C_x, KEY):
    assert (len(KEY) == 16), 'KEY is not the correct size: decryptHex'
    l = []
    for i in range(0, len(C_x), 16):
        c = C_x[i: i + 16]
        D_x = decryptHex(c, KEY)
        D_s = toStr(D_x)
        # yield (D_s)
        l.append(D_s)
    return ''.join(l)

"""
    filename: string eg = 'content.txt'
    KEY: hexadecimal string - 64 bits
"""
def encryptFile(filename, KEY):
    KEY_b = hexToBin(KEY)
    assert (len(KEY_b) == 64), 'Incorrect key'
    l = []
    with open(filename, 'rb') as f:
        while True:
            b = f.read(8)
            if b == b'':    # end of file
                break
            p_b = bytesToBinString(b)
            c_b = encryptBlock(p_b, KEY_b)
            c_x = binToHex(c_b)
            l.append(c_x)
            # yield (c_x)
    return ''.join(l)

"""
    hexArray: ['12bacd..', '144abdd..']
    KEY: hexadecimal string - 64 bits
    returns String
"""
def decryptHexArray(hexArray, KEY):
    assert (len(KEY) == 16), 'KEY is not the correct size: decryptHexArray'
    l = []
    for i in hexArray:
        D_x = decryptHex(i, KEY)
        D_s = toStr(D_x)
        l.append(D_s)
        # yield (D_s)
    return ''.join(l)


if __name__ == '__main__':
    KEY = input('Enter KEY in hexadecimal: ')
    assert (len(KEY) == 16), 'Key is not 64 bits long'

    plaintext = input ('Enter plaintext: ')
    ciphertext = encryptStringToHex(plaintext, KEY)
    print ('\nPlain Text: {}\nCipher Text: {}\n'.format(plaintext, ciphertext))
    
    deciphered = decryptHexToString(ciphertext, KEY)
    print ('\nOn deciphering: {}\n'.format(deciphered))