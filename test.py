from util import toHex, toStr, binToHex, hexToBin
from des import encryptBlock, decryptBlock
KEY = input('Enter 64 bit key in hexadecimal: ')

def encryptStringBlock(P, KEY):
    KEY_b = hexToBin(KEY)
    extra = 8 - len(P) % 8
    P = P + ' ' * (extra)

    P_x = toHex(P)
    P_b = hexToBin(P_x)

    C_b = encryptBlock(P_b, KEY_b)
    C_x = binToHex(C_b)
    # print ('CipherText: {}'.format(C_x))
    return (C_x)

def decryptStringBlock(C_b, KEY):
    KEY_b = hexToBin(KEY)
    D_b = decryptBlock(C_b, KEY_b)
    D_x = binToHex(D_b)
    D_s = toStr(D_x)

    # print ('On decryption: {}'.format(D_s))
    return (D_s)