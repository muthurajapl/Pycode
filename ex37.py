global test, test2
test = 10
test2 = 20

def func1(num):
    print(num)
    num= num * test2
    print(num)
    
print(test2)
func1(test)
#print(num) # error because num is not global

def f(x):
    assert x < 0, 'x must be negative' #assert is used for checking constraints not errors
    return x ** 2


print(f(-2))
#print(f(2)) # error because argument is not negative

with open(r'D:\Personal\Data_Science\Python\Pycode\new_text.txt') as myfile: 
#Automatically closes the file when the block is executed irrespective of whether an error is thrown or not
    for line in myfile:
        print(line)
    else:
        print("All done!")

def gensquares(N): 
#generator that stores the intermediate sequence as an object. This function yields a value, and so returns to its caller, each time through the loop; 
#when it is resumed, its prior state is restored, including the last values of its variables i and N, and control picks up again immediately after the yield 
#statement.
    for i in range(N):
        yield i ** 2 # Resume here later
        
for i in gensquares(5): # Resume the function
    print(i, end=' : ') # Print last yielded value
    
def coroutine():
    for i in range(1, 10):
        print("From generator {}".format((yield i)))
c = coroutine()
c.send(None)
try:
    while True:
        print("From user {}".format(c.send(1)))
except StopIteration: pass


def kaboom(x, y):
    print(x + y) # Trigger TypeError

try:
    kaboom([0, 1, 2], 'spam')
except TypeError: # Catch and recover here
    print('Hello world!')

print('resuming here') # Continue here if exception or not

#class MyError(Exception): pass

#def stuff(file):
 #   raise MyError()    

#file = open('data', 'w') # Open an output file (this can fail too)

#try:
 #   stuff(file) # Raises exception
#finally:
 #   file.close() # Always close file to flush output buffers
#print('not reached') # Continue here only if no exception

sep = '-' * 45 + '\n'

print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

list_str = "[5,6,2,1,6]"
list_str = exec(list_str)
print(list_str)