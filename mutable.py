container = ['a','b','c']
string_build = ""
for data in container:
    string_build += str(data) # inefficient because it is done with immuatable object (string)
print(string_build)
    
builder_list = []
for data in container:
    builder_list.append(str(data)) # efficient because it is done with mutable object (list)
print("".join(builder_list))

t = ("test", builder_list) # the tuple t is itself not mutable. But the list builder_list inside that is mutable
builder_list.append('qrs')
print(t)
 
### Another way is to use a list comprehension
print("".join([str(data) for data in container])) # efficient because it is done with mutable object (list)
 
### or use the map function
print("".join(map(str, container))) # efficient because it is done with mutable object (list)

def my_function(param=[]):
    param.append("thing")
    return param
 
print(my_function()) # returns ["thing"]
print(my_function()) # returns ["thing", "thing"]

def my_function2(param=None):
    if param is None:
        param = []
    param.append("thing")
    return param
       
print(my_function2()) # returns ["thing"]
print(my_function2()) # returns ["thing"]

def updateList(list1):
    list1.append(10)
n = [5, 6]
print(id(n))                  # 140312184155336
updateList(n) # we have called the list via call by reference, so the changes are made to the original list itself
print(n)                      # [5, 6, 10]
print(id(n))                  # 140312184155336
m = []
print(id(m))
updateList(m)
print(m)
print(id(m))

def updateNumber(n):
    print(id(n))
    n += 10
b = 5
print(id(b))                   # 10055680
updateNumber(b)                # 10055680
# The same object is passed to the function, but the variables value doesn’t change even though the object is identical. This is called pass by value. 
# So what is exactly happening here? When the value is called by the function, only the value of the variable is passed, not the object itself. 
# So the variable referencing the object is not changed, but the object itself is being changed but within the function scope only. 
# Hence the change is not reflected.
print(b)                       # 5


