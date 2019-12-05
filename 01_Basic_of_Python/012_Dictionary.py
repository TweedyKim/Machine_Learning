print('===================================================================')
print('|  Dictionary                                                     |')
print('|  01. Definition                                                 |')
print('|  02. Indexing & Add                                             |')
print('|  03. Conversion                                                 |')
print('|  04. Shallow Copy                                               |')
print('|  05. Deep Copy                                                  |')
print('|  06. Get keys, values & items                                   |')
print('|  07. Print Items using by "for"                                 |')
print('|  08. update()                                                   |')
print('|  09. Delete                                                     |')
print('|  10. Search Items using by "in"                                 |')
print('|  11. pprint                                                     |')
print("===================================================================\n\n")



print('1. Definition')
dicA = {'a':1, 'b':2}
dicB = {1:5, 2:3}
dicC = {(1,5):5, (3,3):3}
dicD = {True:5, 'abc':2}
dicE = dict(KDH = 38, JSK = 37, KSJ = 8, KMG =7)
print('    1) dicA is', dicA)
print('       dicB is', dicB)
print('       dicC is', dicC)
print('       dicD is', dicD)
print('       dicE is', dicE, '\n')

print('2. Indexing & Add')
dicA = dict(KDH = 38, JSK = 37, KSJ = 8, KMG =7)
print('    1) dicA is', dicA)
print('       dicA[KDH] is', dicA['KDH'])
dicA['XXX'] = '00'
print('       dicA[XXX] = "00"')
print('       dicA is', dicA, '\n')

print('3. Conversion')
CovA = [['KDH', 38], ['JSK', 37]]
CovB = [('KDH', 38), ('JSK', 37)]
CovC = (('KDH', 38), ('JSK', 37))
CovD = (['KDH', 38], ['JSK', 37])
print('    1) dict(CovA) is', dict(CovA))
print('       dict(CovB) is', dict(CovB))
print('       dict(CovC) is', dict(CovC))
print('       dict(CovD) is', dict(CovD), '\n')

print('4. Shallow Copy')
dicA = {'KDH':[38, 'm'],'JSK':[37, 'f'],'KSJ':[8, 'm'],'KMG':[7, 'm']}
dicB = dicA.copy()
dicC = dict(dicA)
print('    1) dicA is', dicA)
print('       dicB is dicA.copy()')
print('       dicB is', dicB)
dicB['KDH'].append(170)
print('       dicB["KDH"].append(170)')
print('       dicA is', dicA)
print('    2) dicCis dict(dicA)')
print('       dicC is', dicC)
dicC['JSK'].append(165)
print('       dicC["JSK"].append(165)')
print('       dicA is', dicA)
print('       dicB is', dicB, '\n')

print('5. Deep Copy')
import copy
dicA = {'KDH':[38, 'm'],'JSK':[37, 'f'],'KSJ':[8, 'm'],'KMG':[7, 'm']}
dicB = copy.deepcopy(dicA)
print('    1) dicA is', dicA)
print('       dicB is copy.deepcopy(dicA)')
print('       dicB is', dicB)
dicB['KDH'].append(170)
print('       dicB["KDH"].append(170)')
print('       dicA is', dicA)
print('       dicB is', dicB, '\n')

print('6. Get keys, values & items')
dicA = {'KDH':[38, 'm'],'JSK':[37, 'f'],'KSJ':[8, 'm'],'KMG':[7, 'm']}
print('    1) dicA is', dicA)
print('       dicA.keys() is', dicA.keys())
print('       dicA.values() is', dicA.values())
print('       dicA.items() is', dicA.items(),'\n')

print('7. Print Items using by "for"')
dicA = {'KDH':[38, 'm'],'JSK':[37, 'f'],'KSJ':[8, 'm'],'KMG':[7, 'm']}
print('    1) Print key using by "for"')
for key in dicA:
    print('       key:', key)
print('    2) Print value using by "for"')
for val in dicA.values():
    print('       value:', val)
print('    3) Print key & value using by "for"')
for key, val in dicA.items():
    print('       key: [{0}] value: {1}'.format(key,val))        
print('')

print('8. update()')
dicA = {'KDH':[38, 'm'],'JSK':[37, 'f'],'KSJ':[8, 'm'],'KMG':[7, 'm']}
print('    1) dicA is', dicA)
dicA.update({'KDH':[39, 'm'],'JSK':[38, 'f']})
print("       dicA.update({'KDH':[39, 'm'],'JSK':[38, 'f']})")
print('       dicA is', dicA, '\n')

print('9. Delete')
dicA = {'KDH':[38, 'm'],'JSK':[37, 'f'],'KSJ':[8, 'm'],'KMG':[7, 'm']}
print('    1) dicA is', dicA)
del dicA['KDH']
print("       del dicA['KDH']")
print("       dicA is", dicA, '\n')

print('10. Search Items using by "in"')
dicA = {'KDH':[38, 'm'],'JSK':[37, 'f'],'KSJ':[8, 'm'],'KMG':[7, 'm']}
print('    1) dicA is', dicA)
print("       'KDH' in dicA:", 'KDH' in dicA)
print("       'JSK' in dicA:", 'JSK' in dicA)
print("       'KXX' in dicA:", 'KXX' in dicA, '\n')

print('11. pprint')
from pprint import pprint as pp
dicA = {'KDH':[38, 'm'],'JSK':[37, 'f'],'KSJ':[8, 'm'],'KMG':[7, 'm']}
print('    1) dicA is')
print('      ',dicA)
print('       Using by pprint')
print('       ', end='')
pp(dicA)

