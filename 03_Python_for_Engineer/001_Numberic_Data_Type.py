print('===================================================================')
print('|  Numberic Data Type                                             |')
print('|  1.complex                                                      |')
print('|  2.Bitwise operator                                             |')
print('|  3.Logic operator                                               |')
print("===================================================================\n\n")

print('01. complex')
x = 1-2*1j
y = complex(2,3)
print('    1) x is', x)
print('    2) y is', y)
print('    3) x+y is', x+y)
print('    4) The real part of y is', y.real)
print('    5) The imaginary part of y is', y.imag)
print('    6) The conjugate complex of y is', y.conjugate(),end='\n\n')

print('02. Bitwise operator')
x = 0b10001
y = 0b10010
print('    1) x is', bin(x))
print('    2) y is', bin(y))
print('    3) x|y is', bin(x|y))
print('    4) x^y is', bin(x^y))
print('    5) x&y is', bin(x&y))
print('    6) x<<4 is', bin(x << 4))
print('    7) y>>4 is', bin(y >> 4))
print('    8) ~y is', bin(~y), end='\n\n')

print('03. Logic operator')
x = 0b10001
y = 0b10010
print('    1) x is', bin(x))
print('    2) y is', bin(y))
print('    3) x and y is', bin(x and y))
print('    4) x or y is', bin(x or y))
print('    5) not x is', not x)
print('    6) not y is', not y, end='\n\n')

# if x == 0b10001 and y == 0b0:
#     print("1")
# if x == 0b10001 or y == 0b0:    
#     print("2")
# if x is 0b10001 and y is 0b0:
#     print("1")
# if x is 0b10001 or y is 0b0:    
#     print("2")   