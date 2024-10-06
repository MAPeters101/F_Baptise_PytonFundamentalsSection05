l1 = [1,2,3]
l2 = l1[:]
l3 = l1
print(f'l1: {l1}')
print(f'l2: {l2}')
print(f'l3: {l3}')

print(l1 is l2)
print(l2 is l3)
print(l3 is l1)
print('=' * 30)
l2.append(20)
print('l2.append(20)')
print(f'l1: {l1}')
print(f'l2: {l2}')
print(f'l3: {l3}')

l3.append(30)
print('l3.append(30)')
print(f'l1: {l1}')
print(f'l2: {l2}')
print(f'l3: {l3}')
l1.append(10)
print('l1.append(10)')
print(f'l1: {l1}')
print(f'l2: {l2}')
print(f'l3: {l3}')


print('=' * 30)
l1 = [1,2,3]
l2 = l1[:]
l3 = l1.copy()
print('l3 = l1.copy()')
print(f'l1: {l1}')
print(f'l2: {l2}')
print(f'l3: {l3}')
print(f'l1 is l2: {l1 is l2}')
print(f'l1 is l3: {l1 is l3}')
print(f'l2 is l3: {l2 is l3}')
l3.append(30)
print('l3.append(30)')
print(f'l1: {l1}')
print(f'l2: {l2}')
print(f'l3: {l3}')

print('=' * 30)
m1 = [[1,0,0],[0,1,0],[0,0,1]]
m2 = m1.copy()
m3 = m1
print(f'm1: {m1}')
print(f'm2: {m2}')
print(f'm3: {m3}')
print(f'm1 is m2: {m1 is m2}')
print(f'm1 is m3: {m1 is m3}')
print(f'm2 is m3: {m2 is m3}')
m2.append([10,20,30])
print('m2.append([10,20,30])')
print(f'm1: {m1}')
print(f'm2: {m2}')
print(f'm3: {m3}')
print(f'm1[0] is m2[0]: {m1[0] is m2[0]}')
print(f'm1[0] is m3[0]: {m1[0] is m3[0]}')

m2[0].append(-1)
print('m2[0].append(-1)')
print(f'm1: {m1}')
print(f'm2: {m2}')
print(f'm3: {m3}')

print('========== DEEP COPY =========')
from copy import deepcopy
m1 = [[1,0,0],[0,1,0],[0,0,1]]
m2 = deepcopy(m1)
print(f'm1: {m1}')
print(f'm2: {m2}')
print(f'm1 is m2: {m1 is m2}')
print(f'm1[0]: {m1[0]}')
print(f'm2[0]: {m2[0]}')
print(f'm1[0] is m2[0]: {m1[0] is m2[0]}')

m2[0].append(10)
print('m2[0].append(10)')
print(f'm1: {m1}')
print(f'm2: {m2}')

a = (1,2,3)
b = a[:]
print(f'a = {a}')
print(f'b = {b}')
print(f"a is b: {a is b}")









