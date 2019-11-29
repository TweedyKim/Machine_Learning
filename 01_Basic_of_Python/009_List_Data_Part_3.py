print('===================================================================')
print('|  List Data Type                                                 |')
print('|  1. Add                                                         |')
print('|  2. Delete                                                      |')
print("===================================================================\n\n")

print('1. Add')
lstA = list(range(3,12,3))
print('    1) Append()')
print('       lstA is', lstA)
lstA.append('x'*2)
print('       lstA.append("x"*2) is', lstA)
lstA.append(['y']*2)
print('       lstA.append(["y"]*2) is', lstA)
print('    2) insert()')
lstA.insert(1,'*')
print('       lstA.insert(0,"*") is', lstA)
print('    3) extend()')
lstA.extend([100,101])
print('       lstA.extend([100,101]) is', lstA)
print('    4) "+" Operation')
lstA += ['zzz']
print('       lstA += ["zzz"] is', lstA, '\n')

print('2. Remove')
lstA = list(range(3,9,5))*2 + ['soc']*2 + [[38,77]*2]
print('    1) lstA is', lstA)
print('    2) del')
del lstA[1]
print('       del lstA[1] is', lstA)
del lstA[:3]
print('       del lstA[:3] is', lstA)
del lstA[2][1:]
print('       del lstA[2][1:] is', lstA)
del lstA[2]
print('       del lstA[2] is', lstA)
del lstA[lstA.index('soc')]
print('       del lstA[lstA.index("soc")] is', lstA)
lstA.remove('soc')
print('       lstA.remove("soc") is', lstA)