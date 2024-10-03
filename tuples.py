t = (1,2,3)
print(t, type(t))
print(t[0])
print(t[1])
print(t[2])
print(t[-1])
print(len(t))
print(t[len(t)-1])
#t[2] = 40

t = ([1,2], [3,4])

print(t, t[0], type(t[0]))

#t[0] = 100

l = t[0]
print(l)
l[0] = 100
print(l, t)

t[1][1] = 400
print(t)

t = 1, 2
print(t, type(t))

a = 10
b = 20
print(a, b, a+b)

c = a, b, a+b
print(c)

t = ()
print(t, type(t), len(t))

t = tuple()
print(t, type(t), len(t))

l = [1, 2, 3]
t = tuple(l)
print(l, t)

t = 10, 20, 30
l = list(t)
print(l, t)

t = 10, 20, 3, 40
l = list(t)
l[2] = 30
t = tuple(l)
print(t)

t = [1, 2], 30, 40
print(t)
t[0][1] = 20
print(t)
l = list(t)
print(l)

l[0][0] = 10
print(l, t)


