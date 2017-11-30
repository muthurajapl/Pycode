from sys import argv

script, filename = argv

print ("We are going to erase %r" % filename)
print ("If you don't want to do that hit Ctrl-C (^C)")
print ("If you want to do that, hit return")

input ("?")

print ("Opening the file.")
target = open(filename,'w+')

print ("Now I am going to ask you for three lines.")

line1 = input ("Enter line 1: ")
line2 = input ("Enter line 2: ")
line3 = input ("Enter line 3: ")

print ("I am going to write these to the file")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#target.writelines([line1,line2,line3])

print ("And finally we close it.")
#target.close()

#target = open(filename,'r')
target.seek(0)
str = target.read()
print(str)
target.close()

#target = open(filename,'w+')
#print ("Truncating the file. Goodbye!")
#target.truncate()

#str = target.read()
#print (str)

