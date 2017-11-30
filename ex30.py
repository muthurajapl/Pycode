x = int(input("Enter number: "))

if 1 <= x <= 10:
    print ("Less than 10")
elif x in range(11,20):
    print ("Between 11 to 20")
elif x <30:
    print ("Between 20 to 30")
else:
    print (">= 30")