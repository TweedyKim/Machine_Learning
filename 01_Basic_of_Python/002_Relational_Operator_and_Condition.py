print('===================================================================')
print('|  Relational Operator & Condition                                |')
print('|  1.Relational Operator                                          |')
print('|  2.if                                                           |')
print("===================================================================\n\n")

print('01. Relational Operator')
a, b = 3, 5
print('    1) %d == %d is %s' % (a,b,a==b))
print('    2) %d != %d is %s' % (a,b,a!=b))
print('    3) %d >  %d is %s' % (a,b,a>b))
print('    4) %d <  %d is %s' % (a,b,a<b))
print('    5) %d <= %d is %s' % (a,b,a<=b))
print('    6) %d >= %d is %s' % (a,b,a>=b), end='\n\n')

print('02. if')
a, b = 3, 5
if a is b:
    print('    1) %d is %d' % (a,b))
else:
    print('    1) %d is not %d' % (a,b))

a, b = 5, 5
if a is b:
    print('    2) %d is %d' % (a,b))
else:
    print('    2) %d is not %d' % (a,b))    