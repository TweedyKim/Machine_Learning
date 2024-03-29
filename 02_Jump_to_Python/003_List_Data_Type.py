print('===================================================================')
print('|  List Data Type                                                 |')
print('|  1. Indexing                                                    |')
print('|  2. Slicing                                                     |')
print('|  3. Operation                                                   |')
print('|  4. Modified & Remove                                           |')
print('|  5. Functions                                                   |')
print("===================================================================\n\n")

print('01. Indexing')
lstA = list(range(1,4))
lstB = [1,2,3,['a','b','c']]
print('    1) lstA is', lstA)
print('    2) lstB is', lstB )
print('    3) lstA[0] + lstA[1] = ', lstA[0]+lstA[1])
print('    4) lstA[-1] is', lstA[-1])
print('    5) lstB[0] is', lstB[0])
print('    5) lstB[-1] is', lstB[-1])
print('    6) lstB[3] is', lstB[3])
print('    7) lstB[3][1] is', lstB[3][1])
print('    8) lstB[3][-1] is', lstB[3][-1],end='\n\n')

print('02. Slicing')
lstA = list(range(2,20,2))
lstB = list(range(2,12,2)) + list('xyz') + [list(range(1,7,2))]
print('    1) lstA is', lstA)
print('    2) lstB is', lstB )
print('    3) lstA[0:2] is', lstA[0:2])
print('    4) lstA[:2] is', lstA[:2])
print('    5) lstB[:2] is', lstB[:2])
print('    6) lstA[2:] is', lstA[2:])
print('    7) lstB[2:] is', lstB[2:])
print('    8) lstB[8][:2] is', lstB[8][:2],end='\n\n')

print('03. Operation')
lstA = list(range(2,6,2))*3 + ['xa']*3 + [[38,77]*2]
print('    1) lstA is', lstA)
print('    2) len(lstA) is', len(lstA))
print('    3) len(lstA[9]) is', len(lstA[9]))

print('04. Modified & Remove')
lstA = list(range(3,9,5))*2 + ['soc']*2 + [[38,77]*2]
print('    1) lstA is', lstA)
lstA[4] = 8
lstA[3] = 'soc'
print('    2) Modified lstA[4] = "sox" and lstA[3] = "sxx"')
print('       lstA is', lstA)
del lstA[1]
print('    3) del lstA[1] is', lstA)
del lstA[:3]
print('    4) del lstA[:3] is', lstA)
del lstA[2][1:]
print('    5) del lstA[2][1:] is', lstA)
del lstA[2]
print('    6) del lstA[2] is', lstA, end='\n\n')

print('04. Functions')
lstA = list(range(3,12,3))*2
print('    1) Append()')
print('       lstA is', lstA)
lstA.append('x'*2)
print('       lstA.append("x"*2) is', lstA)
lstA.append([2]*2)
print('       lstA.append(["y"]*2) is', lstA, end='\n\n')
lstA.clear()
lstA = list(range(1,10,2))+list(range(2,10,2))
print('    2) Clear lstA and rearrange ->', lstA)
lstA.sort()
print('    3) sort()')
print('       lstA.sort() is', lstA)
lstA.reverse()
print('       lstA.reverse() is', lstA)
lstA.append(['a','b'])
print('       It can not work if int & string is are mixed in list for Sort & Revsers', end='\n\n')
print('    4) Clear lstA and rearrange ->', lstA)
print('    5) index()')
print('       lstA.index(8) is', lstA.index(8))
print('       lstA.index("a") is not working.')
lstA[9].insert(0,'x')
print('    6) insert()')
print('       lstA[9].insert(0,"x") is', lstA)
lstA.insert(0,10)
print('       lstA.insert(0,10) is', lstA)
print('    7) pop()')
print('       lstA.pop(0) is', lstA.pop(0))
print('       lstA is', lstA)
print('       lstA.pop(9) is', lstA.pop(9))
print('       lstA is', lstA)
lstA.extend([100,101])
print('    8) extend()')
print('       lstA.extend([100,101]) is', lstA)
lstA.extend([['l','o']])
print('       lstA.extend([["l","o"]]) is', lstA)
