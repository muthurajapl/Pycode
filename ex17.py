from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s." %(from_file, to_file))

with open(from_file) as in_file:
    in_data = in_file.read()
	
print ("The input is %d bytes long." % len(in_data))

print ("Does the output file exist?", exists(to_file))

print ("Hit return to continue, Ctrl+C to abort.")
input()

out_file = open(to_file, 'w+')
out_file.write(in_data)

out_file.seek(0)
print (out_file.read())
print ("Alright, all done!")

out_file.close()
in_file.close()