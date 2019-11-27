print('===================================================================')
print('|  List Data Type                                                 |')
print('|  1. Repeat                                                      |')
print('|  2. Method                                                      |')
print("===================================================================\n\n")

print('1. Repeat')
lstA = [list(range(3,10,3))] * 2
lstB = lstA * 2
print('    1) lstB = lstA * 2 is shallow copy')
print('       lstA is', lstA)
print('       lstB is', lstB)
print('       id(lstA) is', id(lstA))
print('       id(lstB) is', id(lstB))
print('       id(lstA[1]) is', id(lstA[1]))
print('       id(lstB[1]) is', id(lstB[1]),'\n')

print('2. Method - index() count() in')
lstA = list(range(3,15,3))*3
print('    1) lstA is', lstA)
print('    2) index(12) is', lstA.index(12))
print('    3) count(12) is', lstA.count(12))
print('    4) "12" in lstA is', 12 in lstA)
print('    5) "12" not in lstA is', 12 not in lstA)

# print('02. Copy')
# lstB = lstA[:]
# print('    1) lstB = lstA[:] and lstB is', lstB)
# print('       lstA == lstB is', lstA == lstB)
# print('       lstA is lstB is', lstA is lstB, '\n')
# lstC = lstA.copy()
# lstD = list(lstA)
# print('    2) lstC = lstA.copy() and lstC is', lstC)
# print('       lstA == lstB is', lstA == lstC)
# print('       lstA is lstB is', lstA is lstC,'\n')

