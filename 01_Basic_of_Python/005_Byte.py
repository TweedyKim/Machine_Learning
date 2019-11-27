print('===================================================================')
print('|  Byte & Unicode                                                 |')
print("===================================================================\n\n")


print('1. Byte & Unicode')

TsChr1 = 'Tweedy'
TsChr2 = '김동훈'
print('   1) The length of "{0}" is {1:d}'.format(TsChr1,len(TsChr1)))
print('      Bytes("{}", UTF8) is {}'.format(TsChr1,bytes(TsChr1,'UTF8')))
print('      The length of Bytes("{}", UTF8) is {}'.format(TsChr1,len(bytes(TsChr1, 'UTF8'))))
print('      Bytearray("{}", UTF8) is {}'.format(TsChr1,bytearray(TsChr1,'UTF8')))
print('      The length of Bytearray("{}", UTF8) is {}'.format(TsChr1,len(bytearray(TsChr1, 'UTF8'))),end='\n\n')

print('   2) The length of "{0}" is {1:d}'.format(TsChr2,len(TsChr2)))
print('      Bytes("{}", UTF8) is {}'.format(TsChr2,bytes(TsChr2,'UTF8')))
print('      The length of Bytes("{}", UTF8) is {}'.format(TsChr2,len(bytes(TsChr2, 'UTF8'))))
print('      Bytearray("{}", UTF8) is {}'.format(TsChr2,bytearray(TsChr2,'UTF8')))
print('      The length of Bytearray("{}", UTF8) is {}'.format(TsChr2,len(bytearray(TsChr2, 'UTF8'))),end='\n\n')

TsChr3 = 'Vi er så glad for å høre og lære om Python!'
TsChr4 = TsChr3.encode('utf-8')
print('   3) TsChr3 is {}'.format(TsChr3))
print('      TsChr4 is {}'.format(TsChr4))
print('      Encode TsChr3 for UTF-8 is {}'.format(TsChr3.encode('utf-8')))
print('      Decode TsChr4 for UTF-8 is {}'.format(TsChr4.decode('utf-8')))