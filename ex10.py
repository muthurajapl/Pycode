tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = ('''
"I'll do a list:"
\t* Cat food
\t* Fishies
\t* \rReturned
\t* \bBackspaced
\t* \vVertical tabbed
\t* Catnip\n	* Grass
''')

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

for i in ["/","-","*","\\","|"]:
    print ("%s\r" %i, end = " ")
	
print ("%r" % "\\")
print ("%s" % "\\")
print ("%r" % '\\')
print ("%s" % '\\')