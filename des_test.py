# 		TESTING IMPLEMENTATIONS OF DES
# 		------------------------------

# 		Ronald L. Rivest
# 		MIT Laboratory for Computer Science
# 		Cambridge, Mass. 02139
# 		2/23/85


# ABSTRACT
# --------

# We present a simple way to test the correctness of a DES implementation:
# Use the recurrence relation:

# 	X0      =       9474B8E8C73BCA7D (hexadecimal)

# 	X(i+1)  =       IF  (i is even)  THEN  E(Xi,Xi)  ELSE  D(Xi,Xi)

# to compute a sequence of 64-bit values:  X0, X1, X2, ..., X16.  Here
# E(X,K)  denotes the DES encryption of  X  using key  K, and  D(X,K)  denotes
# the DES decryption of  X  using key  K.  If you obtain

# 	X16     =       1B1A2DDB4C642438

# your implementation does not have any of the 36,568 possible single-fault 
# errors.
from util import binToHex, hexToBin
from des import encryptBlock, decryptBlock

X0 = '9474B8E8C73BCA7D'
X16 = '1B1A2DDB4C642438'

b = hexToBin(X0)
print (binToHex(b))
for i in range(16):
    if i % 2 == 0:
        b = encryptBlock(b, b)
    else:
        b = decryptBlock(b, b)
    print (binToHex(b))

if b == hexToBin(X16):
    print ('\nDES is working.')
else:
    print ('\nDES is not working.')