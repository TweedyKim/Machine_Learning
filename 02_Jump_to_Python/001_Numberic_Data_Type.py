print('===================================================================')
print('|  Numberic Data Type                                             |')
print('|  1.int                                                          |')
print('|  2.float                                                        |')
print('|  3.Octal & Hexadecimal                                          |')
print('|  4.Arithmetic operator                                          |')
print("===================================================================\n\n")

print('01. int')
a, b, c = 123, -178, 0
print('    1) %d' % a)
print('    2) %d' % b)
print('    3) %03d' % c, end='\n\n')

print('02. float')
a, b, c, d = 1.2, -3.45, 4.24E10, 4.24e-10
print('    1) %.3f' % a)
print('    2) %.3f' % b)
print('    3) %.3f' % c)
print('    3) %.3f' % d, end='\n\n')

print('03. Octal & Hexadecimal')
a, b = 0o177, 0x8ff
print('    1) %o = %d' % (a,a))
print('    2) %x = %d' % (b,b), end='\n\n')

print('04. Arithmetic operator')
print('    1) Skip add, minus, multiply and division')
a, b = 2, 10
print('    2) [a=%d] squared [b=%d] is [a**b=%d]' % (a,b,a ** b))
print('    3) [a=%d] squared [b=%d] is [pow(a,b)=%d]' % (a,b,pow(a,b)))
a, b = 20, 8
print('    4) The remainder of [a=%d] division [b=%d] is [a%sb=%d]' % (a,b,"%",a % b))
print('    5) [a=%d] division [b=%d] is [a%sb=%.2f]' % (a,b,"/",a / b))
print('    6) [a=%d] division [b=%d] is [a%sb=%.2f]' % (a,b,"//",a // b))
print('    6) divmode(%d,%d) is (%d,%d)' % (a,b,divmod(a,b)[0],divmod(a,b)[1]))