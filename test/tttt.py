import binascii

import chardet

# with open('C:/Users/v5682/Desktop/configdataAB_Mingwen.dat', 'rb') as f:
#     f_read = f.read()
#     f_charInfo = chardet.detect(f_read)
#     text = f_read.decode(f_charInfo['encoding'])
with open('C:/Users/v5682/Desktop/configdataAB_Mingwen.dat', 'rb') as f:
    text= f.read()


print(str(binascii.hexlify(text)))