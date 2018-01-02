
import numpy as np
import pandas as pd

mylist = [1,2,3]
x = np.array(mylist)

print(x)

m = np.array([[1,2,3],[4,5,6]])
print(m.shape)

n = np.arange(0, 30, 2)
print(n)

n = n.reshape(3,5)
print n

o = np.linspace(0,4,9)
print o

o = o.resize(3,3)
print o

print np.ones((3,2))
print np.zeros((3,2))
print np.eye(5)
print np.diag(x)

p = np.ones((2,3), int)
print np.vstack([p, p*2]), '\n',np.hstack([p, p*2])

s = np.arange(13)**2
print s, s[0], s[4], s[0:3]
print s[1:5]
print s[-4:]
print s[-5::-2]

r = np.arange(36).reshape((6,6))
print r, '\n', r[2,2], r [-1:, -2:]
print r[-1:, ::2], r[r>30]

test1 = np.random.randint(0, 10, (4,3))

for row in test1:
    print row


sports = {
    'Archery': 'Bhutan',
    'Golf': 'Scotland',
    'Sumo': 'Japan',
    'Taekwondo': 'South Korea'
}

s = pd.Series(sports, index = ['Golf', 'Sumo', 'Hockey'])

s = pd.Series(np.random.randint(0, 1000, 1000))
print(s.head())

%%timeit -n 10
for label, value in s.iteritems():
    s.iloc[label] = value + 2