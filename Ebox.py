from Dbox import Dbox

""" 
    Output position: Input position
"""
table = {
    1: 3,
    2: 1,
    3: 2,
    4: 3,
    5: 1
}

def Ebox(binary_string, table = table):
    return Dbox(binary_string, table)