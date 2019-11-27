print('===================================================================')
print('|  List Data Type                                                 |')
print('|  1. Indexing & Slicing                                          |')
print('|  2. Copy                                                        |')
print("===================================================================\n\n")

print('01. Indexing & Slicing')
lstA = list(range(1,11))
print('    1) lstA is', lstA)
print('       lstA[::2] is', lstA[::2])
print('       lstA[::-2] is', lstA[::-2],end='\n\n')

print('02. Copy')
lstB = lstA[:]
print('    1) lstB = lstA[:] and lstB is', lstB)
print('       lstA == lstB is', lstA == lstB)
print('       lstA is lstB is', lstA is lstB, '\n')
lstC = lstA.copy()
lstD = list(lstA)
print('    2) lstC = lstA.copy() and lstC is', lstC)
print('       lstA == lstB is', lstA == lstC)
print('       lstA is lstB is', lstA is lstC,'\n')

print('    3) lstD = list(lstA) and lstD is', lstD)
print('       lstA == lstB is', lstA == lstD)
print('       lstA is lstB is', lstA is lstD)

