from collections import OrderedDict
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print (''.join(d.keys())) # 'acdeb'
d.move_to_end('b', last=False)
print (''.join(d.keys())) # 'bacde'
print (''.join(reversed(d.keys()))) #edcab
#d.popItem()
#print (''.join(d.keys())) # 'bacd'

# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
od1 = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print (od1)
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# dictionary sorted by value
od2 = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
print (od2)
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# dictionary sorted by length of the key string
od3 = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
print (od3)
# OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])
print (list(od1.items())==list(od2.items())) # False