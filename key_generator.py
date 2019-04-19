from Dbox import Dbox

""" INCOMPLETE """
parityDropTable = {
    1: 57, 
    2: 49,
    3: 41,
    4: 33

}
""" INCOMPLETE """
compressionTable = {
    1: 14,
    2: 17,
    3: 11,
    4: 24
}

def Lshift(string):
    f = string[0]
    new_str = string[1:] + f
    return new_str

"""
    keyWithParities: 64 bit binary
    returns list with 16 keys, each of length 48 bits
"""
def key_generator(keyWithParities):
    keys = []
    key = Dbox(keyWithParities, parityDropTable)
    left = key[:28]
    right = key[28:]
    left_shift = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)
    for round in range(16):
        left = Lshift(left)
        right = Lshift(right)
        if left_shift[round] == 2:
            left = Lshift(left)
            right = Lshift(right)
        k = Dbox(left + right, compressionTable)
        keys.append(k)
    return keys