print ("How old are you?", end = " ")
age = input()
print ("How tall are you?", end = " ")
height = input()
print ("How much do you weigh?", end = " ")
weight = input()

print ("So you are %d old %f tall and %f heavy." % (
    int(age), round(float(height),-1), round(float(weight),2)))