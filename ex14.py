from sys import argv

script, username = argv
prompt ='>'

print ("Hi %s, I am the %r script." % (username, script))
print ("I'd like to ask you a few questions")
print ("Do you like me %s?" % username)
likes = input(prompt)

print ("Where do you live?")
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("""
Alright you said %r about liking me.
You said you live in %s. Not sure where it is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))