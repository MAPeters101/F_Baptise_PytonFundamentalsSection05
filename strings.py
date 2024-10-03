a = 'hello'
b = "Python"
c = "Python's best features:"
#d = 'Python's best features:'
e = 'Python\'s best features:'

s = 'Python rocks!'
print(s[0])
print(s[1])
print(s[len(s)-1])
print(s[-1])
print(s[-2])

#s[0] = 'X'

a = ''
b = ""
c = str()
print(a, type(a), len(a), b, type(b), len(b), c, type(c), len(c))

t = (1, 2, 3)
print(t, str(t))
s = str(t)
print(s, len(s), s[0])


s = 'Python'
t = tuple(s)
print(t)

l = list(s)
print(l)

l = ['a', 'b', 'c', 'd', 'e', 'f']
m = list("abcdef")
print(l)
print(m)

s = '=' * 20
print(s)

t = (1, 2, 3) * 3
print(t)

l = [1, 2, 3] * 3
print(l)

l = [0] * 10
print(l)

t = ([1, 2], 30)
t2 = t * 3
print(t2)

print(t2[0] is t[0])
print(t2[2] is t[0])

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print(m[0][0], m[0][1], m[2][2])

row_1 = m[0]
print(row_1)
print(row_1[0])

row_1[0] = 1
print(m)
m[1][1] = 2
m[2][2] = 3
print(m)

m = [[0, 0, 0]] * 3
print(m)
print(m[0] is m[1])

m[0][0] = 1
print(m)

row = [0, 0, 0]
m = [row] * 3
print(m)
m[0][0] = 1
print(row)
print(m)
