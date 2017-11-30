name = "Zed A. Shaw"
age = 35
height1 = 74*2.54
weight = 180.0*0.453592
eyes1 = 'Blue'
teeth = 'White'
hair = 'Brown'

print ("Let's talk about %s." %name)
print ("He's %r cm tall." % round(height1,2))
print ("He's %r kgs heavy." % round(weight,2))
print ("Actually that's not too heavy")
print ("He's got %r eyes and %s hair." % (eyes1,hair))
print ("His teeth are usually %s depending on the coffee." %teeth)

print ("If I add %r,%r and %r I will get %r" % (age,height1,weight,age+height1+weight))

print ("Hello {}, my name is {}".format('john', 'mike'))
#output is 'Hello john, my name is mike'.

print ("{1}, {0}".format('world', 'Hello'))
#output is 'Hello, world'

print ("{greeting}, {}".format('world', greeting='Hello'))
# output is 'Hello, world'
