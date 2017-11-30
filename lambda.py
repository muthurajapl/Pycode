def func(x, y, z): return x + y + z
print(func(2, 3, 4))

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))

a = lambda x = 'fee', y = 'fie', z = 'foe': x + y + z
print(a('wee'))

def knights():
    title = 'Sir'
    action = (lambda x: title+' '+x)
    return action
    
act = knights()
msg = act('Muthu')
print(msg)

L = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

for f in L:
    print(f(2))
    
print(L[0](8))

def f1(x): return x ** 2
def f2(x): return x ** 3 # Define named functions
def f3(x): return x ** 4

L = [f1, f2, f3] # Reference by name

for f in L:
    print(f(2)) # Prints 4, 8, 16

print(L[0](3)) # Prints 9

key = 'got'
dict1 = {'already': (lambda: 2 + 2),
         'got': (lambda: 2 * 4),
         'one': (lambda: 2 ** 6)}
print(dict1[key]())
print(dict1['one']())

dict2 = {'one': 3+2, 'two': 3*4, 'three': 3**6}
print(dict2['two'])

lower = (lambda x, y: x if x < y else y)
higher = (lambda x, y : x if x > y else y)
print(lower('aa','bb'))
print(higher('bb','aaa'))

#####
import sys
showall = lambda x: list(map(sys.stdout.write, x)) # 3.X: must use list
t = showall(['spam\n', 'toast\n', 'eggs\n']) # 3.X: can use print

showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))

showall = lambda x: [print(line, end='') for line in x] # Same: 3.X only
t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))

showall = lambda x: print(*x, sep='', end='') # Same: 3.X only
t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))

#####
def action(x):
    return (lambda y: x + y) # Make and return function, remember x

act = action(99)
print(act)
#<function action.<locals>.<lambda> at 0x00000000029CA2F0>
print(act(2)) # Call what action returned

action = (lambda x: (lambda y: x + y)) #poor readability - avoid nested lambdas
act = action(99)
print(act(3))

print(((lambda x: (lambda y: x + y))(99))(4)) #poor readability - avoid nested lambdas