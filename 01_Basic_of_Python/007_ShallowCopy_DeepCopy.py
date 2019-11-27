print('===================================================================')
print('|  Mutable & Immutable                                            |')
print('|  1. Mutable                                                     |')
print('|  2. Immutable                                                   |')
print("===================================================================\n\n")

print('01. Mutable')
lstA = [1,2,3]
print('    1) lstA is', lstA)
print('       id is', id(lstA))
lstA[1] = 'a'
print('       Change lstA[1]="a" and lstA is', lstA)
print('       id is', id(lstA))

setA = {1,2,3}
print('    2) setA is', setA)
print('       id is', id(setA))
setA |= {4,5,6}
print('       Change setA| = {4,5,6} and setA is', setA)
print('       id is', id(setA), '\n')

print('02. Immutable')
strA = 'Tweedy'
print('    1) strA is', strA)
print('       id is', id(strA))
strA = 'Su'
print('       Change strA[1]="Su" and strA is', strA)
print('       id is', id(strA), '\n')

print('03. Shallow Copy')
lstA = list(range(0,11,2))
lstB = lstA[:]
print('    1) lstA is', lstA)
print('       lstB = lstA[:] is', lstB)
print('       id(lstA) is', id(lstA))
print('       id(lstB) is', id(lstB))
print('       lstA == lstB is', lstA == lstB)
print('       lstA is lstB is', lstA is lstB)
lstB[0] = 100
print('       lstB[0] = 100')
print('       lstA is', lstA)
print('       lstB is', lstB)

lstA = [list('DH')]+[list('SJ')]
lstB = lstA[:]
print('    2) lstA is', lstA)
print('       lstB = lstA[:] is', lstB)
print('       id(lstA) is', id(lstA))
print('       id(lstB) is', id(lstB))
print('       id(lstA[1]) is', id(lstA[1]))
print('       id(lstB[1]) is', id(lstB[1]))
lstB[0] = list('SJ')
print('        =========== lstB[0] = list("SJ") ===========')
print('       lstA is', lstA)
print('       lstB is', lstB)
print('       id(lstA[1]) is', id(lstA[1]))
print('       id(lstB[1]) is', id(lstB[1]))
lstB[0] = ['M','G']
print('        =========== lstB[0] = ["M","G"] ===========')
print('       lstA is', lstA)
print('       lstB is', lstB)
print('       id(lstA[1]) is', id(lstA[1]))
print('       id(lstB[1]) is', id(lstB[1]))
lstA[1].append('*')
print('        =========== lstA[1].append("*") ===========')
print('       lstA is', lstA)
print('       lstB is', lstB)
lstA = [list('DH')]+[list('SJ')]
lstB = lstA.copy()
print('    3) lstA is', lstA)
print('       lstB = lstA.copy() is', lstB)
print('       id(lstA) is', id(lstA))
print('       id(lstB) is', id(lstB))
print('       id(lstA[1]) is', id(lstA[1]))
print('       id(lstB[1]) is', id(lstB[1]),'\n')

print('04. Deep Copy')
import copy
lstA = [list('DH')]+[list('SJ')]
lstB = copy.deepcopy(lstA)
print('    1) lstA is', lstA)
print('       lstB = copy.deepcopy(lstA) is', lstB)
print('       id(lstA) is', id(lstA))
print('       id(lstB) is', id(lstB))
print('       id(lstA[1]) is', id(lstA[1]))
print('       id(lstB[1]) is', id(lstB[1]))




