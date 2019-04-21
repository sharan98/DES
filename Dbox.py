""" 
    Output position: Input position
"""
example = {
    1: 2,
    2: 3,
    3: 1
}

"""
    t: permutation table
    Works as Expansion, Compression or Straight D box
    Eg: Dbox('123', example) -> '231'
"""
def Dbox(binary_string, table = example):
    l = []
    try:
        for input_pos in table.values():
            bit = binary_string[input_pos - 1]
            l.append(bit)
    except IndexError:
        print ('Incorrect table or input string: input string not long enough')
    else:
        return ''.join(l)