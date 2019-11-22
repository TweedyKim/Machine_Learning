print('===================================================================')
print('|  while                                                          |')
print("===================================================================\n\n")

print('01. Relational Operator')
c=5
print('    1) test "while c != 0"')
while c != 0:
    print('       Count "c" is %d' % c)
    c -= 1
print('')

c=5
print('    2) test "while c"')
while c:
    print('       Count "c" is %d' % c)
    c -= 1
print('')

c=5
print('    3) breake (if c==3 then break)')
while c:
    print('       Count "c" is %d' % c)
    if c == 3:
        break
    c -= 1
print('')

c=5
print('    4) continue (if c==3 then break)')
while c:
    print('       Count "c" is %d' % c)
    if c == 3:
        c -= 1
        continue
    print('       on going')
    c -= 1