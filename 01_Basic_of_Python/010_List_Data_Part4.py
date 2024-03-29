print('===================================================================')
print('|  List Data Type                                                 |')
print('|  1. Sort                                                        |')
print("===================================================================\n\n")

print('1. Sort')
lstA = list(range(3,12,3))*2
print('    1) sort()')
lstA.sort()
print('       lstA.sort() is', lstA)
lstA.reverse()
print('       lstA.reverse() is', lstA)
lstA.sort()
print('       lstA.sort() is', lstA)
lstA.sort(reverse=True)
print('       lstA.sort(reverse=True) is', lstA)
lstB = 'I love my family.'.split()
print('       lstB is', lstB)
lstB.sort(reverse=True)
print('       lstB.sort(reverse=True) is', lstB)
lstB.sort()
print('       lstB.sort() is', lstB, '\n')

print('    2) sorted')
lstA = 'I love my family.'.split()
lstB = sorted(lstA)
print('       lstA is', lstA)
print('       lstB is sorted(lstA)')
print('       lstB is', lstB, '\n')

print('    3) reversed')
lstA = 'I love my family.'.split()
lstB = list(reversed(lstA))
print('       lstA is', lstA)
print('       lstB is list(reversed(lstA))')
print('       lstB is', lstB, '\n')
