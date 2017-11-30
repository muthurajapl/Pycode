D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print (D['food']) # Fetch value of key 'food'
D['quantity'] += 1 # Add 1 to 'quantity' value
print (D)

D = {}
D['name'] = 'Bob' # Create keys by assignment
D['job'] = 'dev'
D['age'] = 40
print (D)  # {'age': 40, 'job': 'dev', 'name': 'Bob'}
print(D['name'])

bob1 = dict(name='Bob', job='dev', age=40) # Keywords
print (bob1) # {'age': 40, 'name': 'Bob', 'job': 'dev'}

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Zipping
print (bob2) # {'job': 'dev', 'name': 'Bob', 'age': 40}

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
        'jobs': ['dev', 'mgr'],
        'age': 40.5}
        
print (rec['name']) # 'name' is a nested dictionary
# {'last': 'Smith', 'first': 'Bob'}
print (rec['name']['last']) # Index the nested dictionary
# 'Smith'
print (rec['jobs']) # 'jobs' is a nested list
# ['dev', 'mgr']
print (rec['jobs'][-1]) # Index the nested list
# 'mgr'
rec['jobs'].append('janitor') # Expand Bob's job description in place
print (rec)
# {'age': 40.5, 'jobs': ['dev', 'mgr', 'janitor'], 'name': {'last': 'Smith',
# 'first': 'Bob'}}

rec = 0 # Now the object's space is reclaimed

D = {'a': 1, 'b': 2, 'c': 3}
print (D) # {'a': 1, 'c': 3, 'b': 2}
D['e'] = 99 # Assigning new keys grows dictionaries
print (D) # {'a': 1, 'c': 3, 'b': 2, 'e': 99}
#print (D['f']) # Referencing a nonexistent key is an error
#...error text omitted...
# KeyError: 'f'

print ('f' in D) # False
if not 'f' in D: # Python's sole selection statement
    print('missing')
# missing

value = D.get('x', 0) # Index but with a default
print (value) # 0
value = D['x'] if 'x' in D else 0 # if/else expression form
print (value) # 0

D = {'a': 1, 'b': 2, 'c': 3}
print (D) # {'a': 1, 'c': 3, 'b': 2}
Ks = list(D.keys()) # Unordered keys list
print (Ks) # A list in 2.X, "view" in 3.X: use list()
# ['a', 'c', 'b']
Ks.sort() # Sorted keys list
print (Ks)
# ['a', 'b', 'c']
for key in Ks: # Iterate though sorted keys
    print(key, '=>', D[key]) # <== press Enter twice here (3.X print)
# a => 1
# b => 2
# c => 3

print (D) # {'a': 1, 'c': 3, 'b': 2}
for key in sorted(D):
    print(key, '=>', D[key])
# a => 1
# b => 2
# c => 3


