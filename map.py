counters = [1, 2, 3, 4]

updated = []
for x in counters:
    updated.append(x + 10) # Add 10 to each item

print(updated)

def inc(x): return x + 10

print(list(map(inc, counters)))

print(list(map((lambda x: x + 3), counters)))

def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res
    
print (list(map(inc, [1, 2, 3]))) # Built-in is an iterable

print (mymap(inc, [1, 2, 3])) # Ours builds a list (see generators)

print(list(map(pow, [1, 2, 3], [2, 3, 4]))) # 1**2, 2**3, 3**4

print (list(map(inc, [1, 2, 3, 4])))

print ([inc(x) for x in [1, 2, 3, 4]]) # Use () parens to generate items instead

print ([inc(x) for x in (1, 2, 3, 4)]) 