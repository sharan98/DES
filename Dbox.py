""" 
    Output position: Input position
"""
t = {
    1: 2,
    2: 3,
    3: 1
}

""" 
    t -> permutation table
    Expansion, Compression, Straight
"""
def Dbox(binary_string, table = t):
    l = []
    try:
        for input_pos in table.values():
            bit = binary_string[input_pos - 1]
            l.append(bit)
    except IndexError:
        print ('Incorrect table or input string: input string not long enough')
    else:
        return ''.join(l)